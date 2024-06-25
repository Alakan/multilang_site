# multilang_site

## Installation

```bash
git clone <repository-url>
cd multilang_site
python -m venv env
source env/bin/activate  # ou `.\env\Scripts\activate` sur Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
