import json
import requests
import re
from scans import scan1, scan2, scan3
from concurrent.futures import ThreadPoolExecutor


def concurrent_map(function, iterable):
    with ThreadPoolExecutor(max_workers=len(iterable)) as exec:
        results = exec.map(function, iterable)
    return list(results)


def _process_cve(cve):
    global known_recs
    id = cve["id"]
    r = requests.get(f"https://v1.cveapi.com/{id}.json").json()
    if "This candidate is a duplicate of" in (
        desc := r["cve"]["description"]["description_data"][0]["value"]
    ):
        duplicate_cve = re.findall(r"CVE-\d{4}-\d+", desc)[0]
        return _process_cve({"id": duplicate_cve, "description": ""})
    if "baseMetricV3" in r["impact"].keys():
        version = "V3"
        base_score_v3 = r["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]
        base_severity_v3 = r["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]
    else:
        version = "V2"
        base_score_v3 = ""
        base_severity_v3 = ""
    base_score = r["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
    base_severity = r["impact"]["baseMetricV2"]["severity"]
    return {
        "id": id,
        "description": cve["description"]
        if cve["description"]
        else r["cve"]["description"]["description_data"][0]["value"],
        "versions": r["configurations"]["nodes"],
        "impact_version": version,
        "base_score_v2": base_score,
        "base_severity_v2": base_severity,
        "base_score_v3": base_score_v3,
        "base_severity_v3": base_severity_v3,
        "rec": known_recs[id] if id in known_recs.keys() else "",
    }


def _process_cves(service, cves):
    if not cves:
        return []
    ps = concurrent_map(_process_cve, cves)
    ps_filtered = []
    for p in ps:
        if p["versions"][0]["operator"] == "OR":
            if service in p["versions"][0]["cpe_match"][0]["cpe23Uri"]:
                ps_filtered.append(p)
        else:  # AND
            if service in p["versions"][0]["children"][0]["cpe_match"][0]["cpe23Uri"]:
                ps_filtered.append(p)
    return ps_filtered


def parse_service(s):
    lines = s.split("\n")
    lines = lines[5:]
    port, state, service, reason, *service_display_name, service_version = filter(
        lambda x: x != "", lines[0].split()
    )
    port, proto = port.split("/")
    lines = lines[1:]
    other_vulns = []
    vulns = []
    cves = []
    lines = list(map(lambda s: s.strip("| "), lines))[:-4]
    vulndb = lines[0].strip(":")
    lines = lines[1:]
    for l in lines:
        if len(l) < 5:
            continue
        if l[-1] == ":":
            if vulndb == "MITRE CVE - https://cve.mitre.org":
                cves += vulns
            else:
                other_vulns.append({"vulndb": vulndb, "vulns": vulns})
            vulndb = l.strip(":")
            vulns = []
            continue
        id = l.strip("[").split("]")[0]
        description = "] ".join(l.split("] ")[1:])
        vulns.append({"id": id, "description": description})
        for cve in re.findall(r"CVE-\d{4}-\d+", description):
            cves.append({"id": cve, "description": ""})
    other_vulns.append({"vulndb": vulndb, "vulns": vulns})

    return {
        "port": int(port),
        "proto": proto,
        "state": state,
        "reason": reason,
        "service": service,
        "display_name": " ".join(service_display_name),
        "version": service_version,
        "vulns": other_vulns,
        "cves": _process_cves(service, cves),
    }


known_recs = json.load(open("mongocves.json", "r"))
