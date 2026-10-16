# tinkuy-qhali-registry

Único lugar del ecosistema **tinkuy-qhali** que sabe dónde viven los bytes crudos. Contiene solo **manifiestos y punteros** (DOI, URL, SHA-256), nunca datos. Resolución por hash; `MIRRORS.md` declara quién espeja qué.

- `pointers/<source>-<edition>-<module>.json` — un puntero por archivo crudo (esquema en `schema/pointer.schema.json`).
- `tools/resolve.py` — dado un SHA-256, devuelve las ubicaciones conocidas y verifica el hash tras descargar (Fase 3).
- `tools/verify_mirrors.py` — verificación periódica de mirrors (Fase 3).
- `MIRRORS.md` — quién, qué versión, hash, fecha de verificación.

Licencia: MIT (código y formato de punteros). Los datos a los que apuntan conservan la licencia de su productor. Decisiones: ADR 0002, 0004 y 0007 en `tinkuy-qhali/docs/adr/`.
