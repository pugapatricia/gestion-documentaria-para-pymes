# 🏷️ Proceso de Etiquetado Automático de Documentos  

Este proceso tiene como objetivo **asignar etiquetas inteligentes a documentos** almacenados en OneDrive, evitando depender de rutas o carpetas rígidas.  
El flujo se basa en el uso de un modelo de IA para analizar los archivos, clasificarlos y generar etiquetas útiles para búsquedas posteriores.  

## 🔄 Flujo del proceso  

```mermaid
flowchart TD
    A[Inicio] --> B[Conexion a SharePoint via MS Graph]
    B --> C[Obtener lista de archivos]
    C --> D{El archivo es nuevo o modificado?}

    D -->|Ya etiquetado| L[Buscador IA en Teams o SharePoint]
    D -->|No etiquetado| F[Extraer primeras 500-1000 palabras]

    F --> G[Modelo IA - Clasificacion]
    G --> H[Asignar etiquetas]
    H --> I[Guardar etiquetas en SharePoint]

    F --> J[Generar embeddings del contenido]
    J --> K[Guardar embeddings en Almacen Vectorial]

    I --> L[Actualizar indice de control]
    K --> L[Actualizar indice de control]

    L --> M[Buscador IA en Teams o SharePoint]
    M --> N[Consulta en lenguaje natural]
    N --> O[IA convierte consulta en embeddings]
    O --> P[Busqueda en Almacen Vectorial + Filtro por etiquetas]
    P --> Q[Devolver documentos relevantes con link a SharePoint]

```
