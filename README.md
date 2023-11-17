# 📃 About:

The **FastAPI application** provides an **API** for **finding forms by their fields and data types**. The **TinyDB** database is used to store form templates, as it allows you to **conveniently store a JSON-based data structure**. **Unittests were also written for the project**.

> Initially, the database contains the following forms:
> ```python
> initial_db_data = [
>     {"name": "First form", "email": "EMAIL", "phone": "PHONE"},
>     {"name": "Second form", "email": "EMAIL", "phone": "PHONE", "birth_date": "DATE"},
> ]
> ```

# ❕ URLs
* #### get_form/ - Retrieving a form by its fields.

# 💽 Installation

1. #### Clone or download the repository.
2. #### Install requirements: `pip install -r requirements.txt`
3. #### Run development server: `python main.py`

# 🌄 Demonstration

#### Form is found:

![Postman_Jfv0Rv0hHo](https://github.com/FCTL3314/Completed-Forms-Identifying-Application/assets/97694131/c13807ff-ec9f-4721-af0a-e4180603f9a4)

#### Form is not found:

![Postman_xSEqjKncIZ](https://github.com/FCTL3314/Completed-Forms-Identifying-Application/assets/97694131/4e6477b0-12c9-4b8a-acb7-579f6c800851)
