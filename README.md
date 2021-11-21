# nutrition

[![CircleCI](https://circleci.com/gh/erikdeirdre/nutrition.svg?style=svg)](https://circleci.com/gh/erikdeirdre/nutrition)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/14a718773e304ddeadab8c55d48ea9a0)](https://www.codacy.com/manual/erikdeirdre/nutrition?utm_source=github.com&utm_medium=referral&utm_content=erikdeirdre/nutrition&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0c63e63be3e437d99ce9e5d97f18fb9)](https://www.codacy.com/gh/food1984/nutrition?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=food1984/nutrition&amp;utm_campaign=Badge_Grade)
This is my attempt at learning more `Flask` and `Angular` by creating a recipe system including nutritional information.  

Let's see how far I get with this.

### Troubleshooting

#### Problem
If executing `flask initdb` results in:
```bash
Usage: flask [OPTIONS] COMMAND [ARGS]...
Try "Flask --help" for help.

Error: No such command "initdb".
```

#### Solution
Make sure `FLASK_APP` variable is set to 'nutrition.py'

```bash
export FLASK_APP=nutrition.py
```
