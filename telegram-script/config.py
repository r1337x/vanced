class Config:
    REVANCED_APKS_RELEASE_URL = (
        "https://api.github.com/repos/r1337x/vanced/releases/latest"
    )
    MICROG_RELEASE_URL = (
        "https://api.github.com/repos/TeamVanced/VancedMicroG/releases/latest"
    )
    REVANCED_CHANGES_URL = (
        "https://api.github.com/repos/revanced/revanced-patches/compare"
    )
    REVANCED_EXTENDED_CHANGES_URL = (
        "https://api.github.com/repos/inotia00/revanced-patches/compare"
    )

    NOTES = """*≣ Note:*
 ➜ `mindetach.zip` is used to detach play store updates for YT and YT Music for rooted users.
 ➜ `microg.apk` is used for google services and must be installed for non root YT and YT Music."""
    CREDITS_MESSAGE = "Based on ReVanced Stable"

    RELEASE_MESSAGE = """📑 *RELEASE* {release_name}

{revanced_version_message}

[Release notes and changelogs (What's New)]({changelogs_url})

{notes}

📦 *Downloads* 

Non-Root:
{nonroot_files}

Magisk (Root):
{root_files}

{credits_message}
    
1337x"""
