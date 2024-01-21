from sys import argv
from json import load


def to_markdown(parse_result: dict):
    vuln_num = sum(map(lambda c: len(c["vulns"]), parse_result["vulns"]))
    head = f"""**{parse_result['display_name']}** `v{parse_result['version']}` была найдена на порте `{parse_result['port']}`/`{parse_result['proto']}`, используя `{parse_result['reason']}`. Было обнаружено {vuln_num} уязвимостей и {len(parse_result['cves'])} CVE.
"""
    if parse_result["cves"]:
        head += "# CVE"
    for cve in parse_result["cves"]:
        head += "\n### {}\n".format(cve["id"])
        head += "#### Описание\n"
        head += cve["description"] + "\n"
        head += "#### Оценка по версии 2\n"
        head += "Базовая мера: **{}**\n".format(cve["base_score_v2"])
        head += "Категория: **{}**\n".format(cve["base_severity_v2"])
        if cve["impact_version"] == "V3":
            head += "#### Оценка по версии 3\n"
            head += "Базовая мера: **{}**\n".format(cve["base_score_v3"])
            head += "Категория: **{}**\n".format(cve["base_severity_v3"])
        if cve["rec"]:
            head += "#### Рекомендации по устранению\n"
            head += cve["rec"]
        head += "\n---\n"
    return head


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        j = load(f)
    print(to_markdown(j))
