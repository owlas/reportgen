# Report generator

Just a toy to try to bulid an easy to use alternative to jupyter notebooks.

**Objectives**
 - Reproducible reports
 - One *acton* to create report
 - Scriptable and automated (can be built using CD)
 - Versioned reports
 - Simple API
 - Handles matplotlib and pandas *natively*

### Requires

 - python
 - pdflatex

### Build the report

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
make
```
