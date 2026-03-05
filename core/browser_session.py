"""
Gestión de sesión de navegador: CDP (Chrome existente) o lanzamiento local con Playwright.
Retorna (browser, context, page, session_cdp).
"""

import time

import core.state as state


def _es_pagina_reutilizable(page):
    try:
        url = (page.url or "").strip().lower()
    except Exception:
        return False
    if not url:
        return False
    if url in {"about:blank", "chrome://newtab/", "chrome://new-tab-page/"}:
        return True
    return url.startswith("chrome://newtab")


def _obtener_contexto_cdp(browser, timeout_segundos=8):
    deadline = time.time() + timeout_segundos
    while time.time() < deadline:
        if browser.contexts:
            return browser.contexts[-1]
        time.sleep(0.2)

    try:
        return browser.new_context()
    except Exception as error:
        raise RuntimeError(
            "CDP conectado, pero no hay contexto de navegador listo todavía. "
            "Reintenta en unos segundos."
        ) from error


def _obtener_pagina_existente(context, timeout_segundos=3):
    deadline = time.time() + timeout_segundos
    while time.time() < deadline:
        if context.pages:
            pagina = context.pages[0]
            try:
                if not pagina.is_closed():
                    return pagina
            except Exception:
                pass
        time.sleep(0.2)
    return None


def _crear_sesion_navegador(playwright):
    if state.CFG.get("usar_chrome_existente"):
        cdp_url = state.CFG.get("cdp_url") or "http://127.0.0.1:9222"
        print(f"🔌 Conectando a Chrome existente por CDP: {cdp_url}")
        try:
            browser = playwright.chromium.connect_over_cdp(cdp_url)
        except Exception as error:
            raise RuntimeError(
                f"No se pudo conectar a Chrome por CDP en {cdp_url}. "
                "Inicia Chrome con --remote-debugging-port=9222 e inténtalo de nuevo."
            ) from error
        context = _obtener_contexto_cdp(browser)
        if state.CFG.get("cdp_reutilizar_primera_pestana"):
            page = _obtener_pagina_existente(context)
            if page and _es_pagina_reutilizable(page):
                try:
                    page.bring_to_front()
                except Exception:
                    pass
                print("🧭 CDP conectado: usando la primera pestaña disponible.")
            else:
                page = context.new_page()
                print("🧭 CDP conectado: pestaña inicial no reusable; se abrió una nueva.")
        else:
            page = context.new_page()
            print("🧭 CDP conectado: se abrió una pestaña nueva para esta ejecución.")
        return browser, context, page, True

    browser = playwright.chromium.launch(headless=state.CFG["headless"], slow_mo=state.CFG["slow_mo"])
    context = browser.new_context()
    page = context.new_page()
    return browser, context, page, False
