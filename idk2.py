from seleniumbase import Driver
driven=Driver(uc=True, headless=True)
driven.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )


