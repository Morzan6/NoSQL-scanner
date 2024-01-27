from sys import argv
from json import load


def to_markdown(parse_result: dict):
    vuln_num = sum(map(lambda c: len(c["vulns"]), parse_result["vulns"]))
    head = f"""**{parse_result['display_name']}** `v{parse_result['version']}` была найдена на порте `{parse_result['port']}`/`{parse_result['proto']}`. Было обнаружено {vuln_num} уязвимостей и {len(parse_result['cves'])} CVE. \n\n
"""
    if parse_result["cves"]:
        head += "# CVE"
    for cve in parse_result["cves"]:
        head += "\n### {}\n".format(cve["id"])
        head += "#### Описание\n"
        head += cve["description"] + "\n\n"
        head += "#### Оценка по версии 2\n\n"
        head += "Базовая мера: **{}**\n\n".format(cve["base_score_v2"])
        head += "Категория: **{}**\n\n".format(cve["base_severity_v2"])
        if cve["impact_version"] == "V3":
            head += "#### Оценка по версии 3\n\n"
            head += "Базовая мера: **{}**\n\n".format(cve["base_score_v3"])
            head += "Категория: **{}**\n\n".format(cve["base_severity_v3"])
        if cve["rec"]:
            head += "#### Рекомендации по устранению\n\n"
            head += cve["rec"]
        head += "\n---\n"
        
    if parse_result["vulns"]:
        head += "# Другие уязвимости"
    for vulndb in parse_result["vulns"]:
        for vuln in vulndb["vulns"]:
            head += "\n### {}\n".format(vuln["description"])
            head += "\n---\n"
    return head


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        j = load(f)
    print(to_markdown(j))
