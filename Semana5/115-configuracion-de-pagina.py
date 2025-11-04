def configurar_pagina(**kwargs):
    tema = kwargs.get("tema","claro")
    idioma = kwargs.get("idioma","espanol")
    print(f"Configuracion -> tema {tema}, idioma {idioma}")

configurar_pagina(tema="oscuro")
configurar_pagina()