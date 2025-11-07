### Laboratorio: Pruebas en Infraestructura como código (IaC)

1. **Pruebas de contrato** (`pruebas_contrato/`)

#### Requisitos previos

- Python 3.8+ instalado  
- Crear un entorno virtual:
  ```bash
  python3 -m venv bdd
  source bdd/Scripts/activate
    ```

**Instalar dependencias**

  ```bash
  pip install pytest jsonschema netaddr ipaddress requests
  ```

#### 1. Pruebas de contrato

Ubicación: `pruebas_contrato/`

Valida el esquema JSON mínimo para módulos de red y servidor locales:

```bash
# Generar JSON de red local
python3 pruebas_contrato/main.py --name=testnet --cidr=10.0.0.0/24 --out=pruebas_contrato

# Ejecutar tests de contrato
pytest pruebas_contrato
```
<img width="1578" height="257" alt="image" src="https://github.com/user-attachments/assets/8f9ee184-9280-4d70-8c76-0332e45f0c9a" />

