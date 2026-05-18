from __future__ import annotations

import re
from pathlib import Path

FILE_PATH = Path("Vulnerabilidade_Maio2026.csv")
ENCODINGS = ("utf-8-sig", "cp1252", "latin-1")

FALLBACK_ACTION = (
    "Avaliar e aplicar atualização para versão corrigida do componente afetado "
    "conforme advisory de segurança informado no título."
)


def detect_encoding(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for encoding in ENCODINGS:
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace"), "latin-1"


def is_vulnerability_line(line: str, line_number: int) -> bool:
    if line_number == 0:
        return False
    if ";" not in line:
        return False
    if line.startswith('";\'-;;;;'):
        return False

    parts = line.split(";")
    if len(parts) < 7:
        return False

    owner = parts[0].strip()
    owner_server = parts[1].strip()

    if not owner or not owner_server:
        return False

    if not re.fullmatch(r"[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*", owner):
        return False

    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*", owner_server))


def remediation_for_title(title: str) -> str:
    value = title.lower()

    if "handlebars" in value:
        return (
            "Atualizar o pacote handlebars para a versão >= 4.7.7 via npm update handlebars. "
            "Remover arquivos ZIP e backup desatualizados dos diretórios temporários e lixeira."
        )

    if "pug-code-gen" in value or re.search(r"\bpug\b", value):
        return (
            "Atualizar o pacote pug para a versão >= 3.0.3 via npm update pug. "
            "Atualizar pug-code-gen para >= 3.0.3."
        )

    if re.search(r"\bsend\b", value):
        return "Atualizar o pacote send para a versão >= 0.19.0 via npm update send."

    if "https-proxy-agent" in value:
        return (
            "Atualizar o pacote https-proxy-agent para a versão >= 2.2.3 "
            "via npm update https-proxy-agent."
        )

    if "bootstrap" in value:
        if "ghsa-vxmc" in value:
            return (
                "Atualizar bootstrap para versão >= 5.x ou aplicar mitigações de CSP. "
                "Avaliar upgrade para Bootstrap 5."
            )
        if "ghsa-3mgp" in value:
            return "Atualizar bootstrap para a versão >= 3.4.0 via npm update bootstrap."
        if ".net" in value or "nuget" in value:
            return "Atualizar pacote NuGet bootstrap para >= 3.4.0 via Update-Package bootstrap."

    if re.search(r"\bdiff\b", value):
        return "Atualizar o pacote diff para a versão >= 3.5.1 via npm update diff."

    if "select2" in value:
        return "Atualizar o pacote select2 para a versão >= 4.0.6 via npm update select2."

    if "on-headers" in value:
        return "Atualizar o pacote on-headers para a versão >= 1.1.0 via npm update on-headers."

    if "constantinople" in value:
        return (
            "Atualizar o pacote constantinople para a versão >= 3.1.1 "
            "via npm update constantinople."
        )

    if "js-yaml" in value:
        if "ghsa-2pr6" in value:
            return "Atualizar js-yaml para >= 3.13.0 via npm update js-yaml."
        if "ghsa-mh29" in value:
            return "Atualizar js-yaml para >= 3.14.2 via npm update js-yaml."
        if "ghsa-8j8c" in value:
            return "Atualizar js-yaml para >= 3.13.1 via npm update js-yaml."

    if "clean-css" in value:
        return "Atualizar o pacote clean-css para a versão >= 4.1.11 via npm update clean-css."

    if "brace-expansion" in value:
        return (
            "Atualizar o pacote brace-expansion para a versão >= 1.1.12 "
            "via npm update brace-expansion."
        )

    if "jquery-ui" in value:
        return "Atualizar o pacote jquery-ui para a versão >= 1.13.0 via npm update jquery-ui."

    if "underscore.string" in value:
        return (
            "Atualizar o pacote underscore.string para a versão >= 3.3.5 "
            "via npm update underscore.string."
        )

    if "nwmatcher" in value:
        return "Atualizar o pacote nwmatcher para a versão >= 1.4.4 via npm update nwmatcher."

    if "tunnel-agent" in value:
        return "Atualizar o pacote tunnel-agent para a versão >= 0.6.0 via npm update tunnel-agent."

    if re.search(r"\bdebug\b", value):
        return "Atualizar o pacote debug para a versão >= 2.6.9 via npm update debug."

    if "serve-static" in value:
        return (
            "Atualizar o pacote serve-static para a versão >= 1.16.0 "
            "via npm update serve-static."
        )

    if re.search(r"\bpostcss\b", value):
        return "Atualizar o pacote postcss para a versão >= 8.4.31 via npm update postcss."

    if re.search(r"\bqs\b", value):
        return "Atualizar o pacote qs para a versão >= 6.7.3 via npm update qs."

    if re.search(r"\bajv\b", value):
        return "Atualizar o pacote ajv para a versão >= 6.12.3 via npm update ajv."

    if "parse-uri" in value or "parseuri" in value:
        return (
            "Não há versão corrigida disponível. Remover ou substituir a dependência parseuri "
            "por alternativa segura, como URL nativa do Node.js."
        )

    if "urllib3" in value:
        return "Atualizar urllib3 para >= 2.5.0 via pip install --upgrade urllib3."

    if re.search(r"\bpip\b", value):
        return "Atualizar pip para >= 25.3 via python -m pip install --upgrade pip."

    if "cryptography" in value:
        if "ghsa-79v4" in value:
            return "Atualizar cryptography para >= 44.0.1 via pip install --upgrade cryptography."
        if "ghsa-9v9h" in value:
            return "Atualizar cryptography para >= 42.0.2 via pip install --upgrade cryptography."

    if "commons-lang:commons-lang" in value:
        if "ghsa-j288" in value:
            return (
                "Avaliar migração de commons-lang 2.x para commons-lang3 e atualizar "
                "dependências no pom.xml."
            )
        return (
            "Migrar de commons-lang 2.x para commons-lang3 >= 3.18.0. "
            "Atualizar pom.xml substituindo a dependência."
        )

    if "commons-lang3" in value:
        return "Atualizar org.apache.commons:commons-lang3 para >= 3.18.0 no pom.xml."

    if "commons-configuration" in value:
        return (
            "Avaliar upgrade ou migração para commons-configuration2. "
            "Não há versão corrigida disponível para 1.x e é necessário monitorar CVE."
        )

    if "hibernate-validator" in value or "org.hibernate.validator" in value:
        if "ghsa-rmrm" in value:
            return "Atualizar hibernate-validator para >= 6.0.20.Final no pom.xml."
        if "ghsa-7v6m" in value:
            return "Atualizar hibernate-validator para >= 6.2.0.CR1 no pom.xml."
        if "ghsa-x83m" in value:
            return "Atualizar hibernate-validator para >= 6.2.0.Final no pom.xml."
        return "Atualizar hibernate-validator para a versão corrigida conforme o GHSA específico."

    if "azure.identity" in value:
        if "ghsa-m5vv" in value:
            return (
                "Atualizar pacote NuGet Azure.Identity para >= 1.11.4 e "
                "Microsoft.Identity.Client para >= 4.60.4."
            )
        if "ghsa-wvxc" in value:
            return "Atualizar pacote NuGet Azure.Identity para >= 1.11.0."

    if "microsoft.rest.clientruntime" in value:
        return "Atualizar pacote NuGet Microsoft.Rest.ClientRuntime para >= 2.3.24."

    if "microsoft.identity.abstractions" in value:
        return (
            "Atualizar pacote NuGet Microsoft.Identity.Abstractions para >= 9.0.0 via "
            "Update-Package Microsoft.Identity.Abstractions. Restringir acesso a logs "
            "e evitar LogLevel = Information para Microsoft.Identity.Web."
        )

    if "hadoop-common" in value:
        if "ghsa-8r28" in value:
            return "Atualizar org.apache.hadoop:hadoop-common para >= 2.6.4 no pom.xml."
        if "ghsa-g48f" in value:
            return "Atualizar org.apache.hadoop:hadoop-common para >= 2.6.5 no pom.xml."
        if "ghsa-f5fw" in value:
            return "Atualizar org.apache.hadoop:hadoop-common para >= 3.4.0 no pom.xml."

    if "guava" in value:
        if "ghsa-mvr2" in value:
            return "Atualizar com.google.guava:guava para >= 24.1.1-android no pom.xml."
        if "ghsa-5mg8" in value:
            return "Atualizar com.google.guava:guava para >= 32.0.0-android no pom.xml."

    if "hive-exec" in value:
        if "ghsa-2g9q" in value:
            return "Atualizar org.apache.hive:hive-exec para >= 2.1.2 no pom.xml."
        if "ghsa-rxmr" in value or "ghsa-p639" in value:
            return "Atualizar org.apache.hive:hive-exec para >= 2.3.3 no pom.xml."
        if "ghsa-c476" in value:
            return "Atualizar org.apache.hive:hive-exec para >= 4.0.1 no pom.xml."

    if "org.iq80.snappy" in value or re.search(r"\bsnappy\b", value):
        return "Atualizar org.iq80.snappy:snappy para >= 0.5 no pom.xml."

    if "electron" in value:
        return "Atualizar Azure Data Studio para versão mais recente que inclua Electron >= 28.3.2."

    if "markdown" in value:
        return (
            "Atualizar Azure Data Studio para versão mais recente com correção para "
            "GHSA-wx77-rp39-c6vg."
        )

    if "spring framework" in value:
        if "cve-2022-22950" in value:
            return (
                "Atualizar Spring Framework para >= 5.3.18 ou >= 5.2.20.RELEASE "
                "no pom.xml."
            )
        if "cve-2022-22971" in value:
            return (
                "Atualizar Spring Framework para >= 5.3.19 ou >= 5.2.21.RELEASE "
                "no pom.xml."
            )
        if "cve-2022-22952" in value or "spel" in value:
            return "Atualizar Spring Framework para versão corrigida >= 5.3.x mais recente no pom.xml."

    return FALLBACK_ACTION


def ensure_single_remediation_field(base: str, action: str) -> str:
    action_suffix = f";{action}"

    while base.endswith(action_suffix):
        candidate = base[: -len(action_suffix)]
        if not candidate.endswith(action_suffix):
            break
        base = candidate

    if base.endswith(";"):
        return f"{base}{action}"

    if base.endswith(action_suffix):
        return base

    prefix, separator, _existing_remediation = base.rpartition(";")
    return f"{prefix}{action_suffix}" if separator else f"{base}{action_suffix}"


def transform_file(path: Path) -> int:
    content, encoding = detect_encoding(path)
    lines = content.splitlines(keepends=True)

    transformed = []
    vulnerability_rows = 0

    for idx, original in enumerate(lines):
        base = original.rstrip("\r\n")
        eol = original[len(base) :]

        if idx == 0 and ";" in base:
            if not base.endswith(";Ação Corretiva"):
                base = f"{base};Ação Corretiva"
            transformed.append(base + eol)
            continue

        if is_vulnerability_line(base, idx):
            parts = base.split(";")
            title = parts[6].strip() if len(parts) > 6 else ""
            action = remediation_for_title(title)
            base = ensure_single_remediation_field(base, action)
            vulnerability_rows += 1

        transformed.append(base + eol)

    path.write_text("".join(transformed), encoding=encoding, newline="")
    return vulnerability_rows


def main() -> None:
    rows = transform_file(FILE_PATH)
    print(f"Arquivo atualizado: {FILE_PATH} | Linhas de vulnerabilidade processadas: {rows}")


if __name__ == "__main__":
    main()
