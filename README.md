# CustomRomBot

A fully customizable modular Telegram bot written in [Python](https://www.python.org/) using [python-telegram-bot](https://docs.python-telegram-bot.org/) to help in Custom Rom support groups in getting info about their Officially Supported Devices.

## Installation

### 1. Clone this repository

```sh
git clone https://github.com/PrajjuS/CustomRomBot
cd CustomRomBot
```

### 2. Install required dependencies

```sh
pip install -r requirements.txt
```

### 3. Copy `sample_config.yaml` to `config.yaml`

```sh
mv sample_config.yaml config.yaml
```

### 4. Fill all the variables in `config.yaml`

- `bot_token`: The API token for your Telegram bot.

- `gh_token`: Your GitHub Personal Access Token.

- `rom_name`: The name of the Custom Rom.

- `channel_username`: The username of the Rom's Telegram channel (without the @ symbol).

- `support_group_username`: The username of the Rom's Telegram support group (without the @ symbol).

- `website_url`: The official website URL of the Rom.

- `official_devices_repo`: The repository URL containing the list of officially supported devices in the format `username/repo_name` (without `https://github.com`).

- `device_json_paths`: A list of file paths where device JSON files are present.

- `show_device_infos_of_all_paths`: Boolean (`true`/`false`) that specifies whether to display information from all JSON paths in `device_json_paths` or not (Use it only if there are multiple paths).

- `device_json_structure`: The structure of the Rom's device JSON files.

- `message_format`: Template for bot's message using placeholders corresponding to fields in the device JSON that uses `markdown formatting` (Refer the formatting rules below for more info).

    <details>
        <summary>
            Formatting Rules
        </summary>

  - **Bold Text:** Wrap text in asterisk `*` (eg: `*bold*`).
  - **Italic Text:** Wrap text in underscore `_` (eg: `_italic_`).
  - **Code:** Wrap text in backticks `` ` `` (eg: `` `code` ``).
  - **Code Blocks:** Use triple backticks `` ``` `` for code blocks (eg: `` ```code block``` ``).
  - **Lists:** Use `-` or `*` for unordered lists, and `1.` for ordered lists (eg: `- List`).
  - **Links:** Format links using `[text](URL)` (eg: `[Google](https://www.google.com)`).
  - **Buttons:** Create buttons using `[[text | URL]]` (eg: `[[Google | https://google.com ]]`).
    - To add multiple buttons in a single line:

        ```md
        [[Button Text | URL]] [[Another Button | URL]]
        ```

    - To add multiple buttons in multiple lines:

        ```md
        [[Button Text | URL]]
        [[Another Button | URL]]
        ```

    </details>

**NOTE:** You can refer the example yaml configs below.

<details>
    <summary>
    Example <code>config.yaml</code>
    </summary>

#### Project-Elixir Configs

```yaml
bot_token: "123123123:ssfasjhdfajkshdfjaskhsAASDASDfad"
gh_token: "asdjhfgaskjdhfgjkashdgf"
rom_name: "Project-Elixir"
channel_username: "Elixir_Updates"
support_group_username: "Elixir_Discussion"
website_url:  "https://projectelixiros.com"
official_devices_repo: "ProjectElixir-Devices/official_devices"
device_json_paths:
    - "builds"
show_device_info_of_all_paths: false
device_json_structure: {
    "error": ,
    "filename": "",
    "datetime": ,
    "size": ,
    "url": "",
    "filehash": "",
    "version": "",
    "id": "",
    "tg_username": "",
    "device_name": "",
    "device": "",
    "xda_thread": "",
    "is_active":
}
message_template: |
    *Project Elixir {version} for {device_name}* *(*`{device}`*)*
    *Maintainer:* [{tg_username}](https://t.me/{tg_username})
    *Latest Build:* `{filename}`
    *Is Active:* `{is_active}`

    *Do consider donating if you want to appreciate our work*
    *UPI:* `dwarmachine24@oksbi`

    [[Paypal | https://www.paypal.me/uglykid24]] [[BMC | https://www.buymeacoffee.com/uglykid]] [[Patreon | https://www.patreon.com/join/uglykid24]]
    [[Changelog | https://github.com/ProjectElixir-Devices/official_devices/tree/A14/changelogs/{device}/{filename}.txt]] [[XDA | {xda_thread}]]
    [[Download | https://projectelixiros.com/device/{device}]]
```

#### DroidX-UI Configs

```yaml
bot_token: "112312312:jhasKJDHAKJHajkdhjkahsd"
gh_token: "sdfgasdfasdfsadfsadfasdfasdf "
rom_name: "DroidX-UI"
channel_username: "DroidXUI_announcements"
support_group_username: "DroidXUI_chats"
website_url:  "https://zirgomhaidar.github.io/DxWeb"
official_devices_repo: "DroidX-UI-Devices/vendor_droidxOTA"
device_json_paths:
- "builds/gapps"
- "builds/vanilla"
show_device_info_of_all_paths: true
device_json_structure: {
    "response": [
        {
            "maintainer": "",
            "oem": "",
            "device": "",
            "version": "",
            "filename": "",
            "download": "",
            "timestamp": ,
            "md5": "",
            "sha256": "",
            "size": ,
            "buildtype": "",
            "forum": "",
            "telegram": ""
        }
    ]
}
message_template: |
    *DroidX-UI {version} for {oem} {device}*
    *Maintainer:* [{maintainer}](https://t.me/{maintainer})
    *Latest Build:* `{filename}`
    *MD5:* `{md5}`

    [[Changelog | https://github.com/DroidX-UI-Devices/vendor_droidxOTA/tree/14/changelogs/{filename}.txt]] [[Download | {download}]]
```

</details>

### 5. Run the bot

```sh
python3 -m RomBot
```

## Demo

An example of how this bot works can be seen in [Project-Elixir Support](https://telegram.me/Elixir_Discussion), or you can directly check by messaging the bot at [Elixie](https://telegram.me/projectelixir_bot).

## Support

For any issues regarding the bot, you can approach for help via the following options:

- **Group:** You can reach out [NoobStuffs](https://telegram.me/NoobStuffs)
- **Direct:** You can contact me directly [Here](https://telegram.me/PrajjuS)
