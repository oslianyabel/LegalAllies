# Legal Allies - Frontend Replicado

Este proyecto replica el frontend del sitio web [legalallies.es](https://legalallies.es) en Django.

## Características

### Diseño y Estilo
- **Colores**: Esquema de colores morado (#3d1f5c) y dorado (#d4af37)
- **Responsive**: Totalmente adaptable a dispositivos móviles y tablets
- **Animaciones**: Transiciones suaves y efectos hover

### Páginas Implementadas
1. **Home (/)**: Página principal con:
   - Hero section con imagen principal
   - Tarjetas informativas
   - Grid de servicios/categorías
   - Formulario de contacto en el footer

2. **Detalle de Categoría (/category/<id>/)**: 
   - Banner de categoría
   - Grid de artículos relacionados

3. **Detalle de Artículo (/article/<id>/)**:
   - Breadcrumb de navegación
   - Contenido del artículo con editor rico (CKEditor)
   - Material complementario (video, PDF)
   - Artículos relacionados en sidebar

### Componentes
- **Header**: 
  - Logo
  - Selector de idiomas (15 idiomas)
  - Botón de inicio de sesión
  
- **Footer**:
  - Información de contacto
  - Formulario de contacto
  - Copyright

- **Social Float**: Botones flotantes de redes sociales

## Instalación y Configuración

### 1. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Crear superusuario
```bash
python manage.py createsuperuser
```

### 3. Cargar datos iniciales
Accede al admin de Django en `/admin` y crea:
- **HomeConfiguration**: Configuración de la página principal
- **Categories**: Categorías de servicios
- **SocialNetwork**: Redes sociales
- **Articles**: Artículos para cada categoría

### 4. Configurar archivos media
Asegúrate de tener las carpetas necesarias:
```bash
mkdir media
mkdir media\categories
mkdir media\articles
mkdir media\home
mkdir media\social_networks
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

Accede a `http://localhost:8000`

## Estructura del Proyecto

```
legalallies/
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── category_detail.html
│   │   └── article_detail.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── legalallies/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Modelos Principales

### HomeConfiguration
Configuración general del sitio (logo, imágenes, textos, contacto)

### Category
Categorías de servicios legales (Extranjería, Derecho Civil, etc.)

### Article
Artículos informativos por categoría con soporte para material complementario

### SocialNetwork
Redes sociales para mostrar en el footer flotante

### ComplementaryMaterial
Material adicional (videos, PDFs) asociado a artículos

## Funcionalidades Adicionales

### Internacionalización
El proyecto está preparado para múltiples idiomas usando `django-modeltranslation`:
- Español (ES)
- Inglés (EN)
- Francés (FR)
- Árabe (AR)
- Y 11 idiomas más...

### Editor Rico
Los artículos usan CKEditor para contenido HTML enriquecido.

### Formulario de Contacto
Sistema de envío de mensajes desde el footer (configurable para enviar emails).

## Próximos Pasos

1. Configurar sistema de emails para el formulario de contacto
2. Implementar sistema de autenticación completo
3. Agregar panel de usuario
4. Implementar búsqueda de artículos
5. Agregar sistema de comentarios
6. Implementar newsletter

## Tecnologías Utilizadas

- Django 5.2
- django-modeltranslation
- django-ckeditor
- SQLite (desarrollo)
- CSS3 con CSS Variables
- HTML5 semántico

## Créditos

Frontend replicado de [legalallies.es](https://legalallies.es)
