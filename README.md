#  Aurea Inmuebles
> Tu nuevo hogar, más cerca de lo que crees.

Aurea Inmuebles es una plataforma web inmobiliaria basada en Django, diseñada para mostrar servicios inmobiliarios, propiedades, blog y contenido corporativo, con un panel de administración completo y un diseño moderno y responsive.

---

##  Demo en producción
🔗 **Sitio web online:**  
https://aurea-inmuebles.onrender.com

---

## 📸 Capturas
*(Agrega imágenes si quieres)*  
Ejemplo:

| Home | Admin |
|------|-------|
| ![](./screenshots/home.png) | ![](./screenshots/admin.png) |

---

## 📌 Características
✔ Panel de administración Django  
✔ Gestión de servicios, portafolio y contenido dinámico  
✔ Blog integrado  
✔ Formulario de contacto  
✔ Sistema multimedia para imágenes  
✔ Responsive con Bootstrap  
✔ Deploy automatizado en Render  
✔ Auto-superuser en producción  

---

##  Tecnologías utilizadas
| Área | Herramientas |
|------|--------------|
| Backend | Django, Python |
| Frontend | HTML5, CSS3, Bootstrap |
| Base de datos | SQLite (dev) |
| Deploy | Render |
| Control de versiones | Git + GitHub |

---

##  Estructura del proyecto
webempresa/
│
├── blog/
├── contact/
├── core/
├── pages/
├── services/
├── social/
├── webempresa/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md

yaml
Copiar código

---

##  Instalación en local

### 1. Clona el repositorio
```bash
git clone https://github.com/aimanjr77tech/business-website.git
cd business-website
2. Crea un entorno virtual
bash
Copiar código
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
3. Instala dependencias
bash
Copiar código
pip install -r requirements.txt
4. Aplica migraciones
bash
Copiar código
python manage.py migrate
5. Crea superusuario (solo local)
bash
Copiar código
python manage.py createsuperuser
6. Ejecuta el servidor
bash
Copiar código
python manage.py runserver
 Variables de entorno esperadas
Si usas Render u otro servicio similar:

ini
Copiar código
DEBUG=False
SECRET_KEY=tu_clave_secreta
ALLOWED_HOSTS=aurea-inmuebles.onrender.com
(Agrega más si es necesario)

 Usuario admin en producción
Este proyecto incluye un script para crear automáticamente el usuario admin en Render al hacer deploy.

** Contacto
 Autor: Aiman Benslaiman
 Email: aimanecom77@gmail.com
 GitHub: https://github.com/aimanjr77tech
 Portfolio: 

