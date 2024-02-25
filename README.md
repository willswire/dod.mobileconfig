# dod.mobileconfig

**TL;DR** Download the `dod.mobileconfig` asset from the [latest release page](https://github.com/willswire/dod.mobileconfig/releases/latest), and [install it on your system](https://support.apple.com/guide/mac-help/configuration-profiles-standardize-settings-mh35561/mac#:~:text=Install%20a%20configuration%20profile%20you%27ve%20received&text=Choose%20Apple%20menu%20%3E%20System%20Settings,or%20other%20information%20during%20installation.).

`dod.mobileconfig` is an automated tool designed to simplify the process of trusting Department of Defense (DoD) websites on macOS devices. This tool automatically downloads the latest DoD PKI (Public Key Infrastructure) Certificate Authority (CA) certificates, extracts them, and incorporates them into a `.mobileconfig` file. This file can then be used to easily configure macOS devices to trust all websites with certificates signed by the DoD CA.

## Features

- **Automatic Updates**: Utilizes GitHub Actions to periodically check for and download the latest DoD CA certificates.
- **Seamless Integration**: Extracts and embeds certificate data directly into the `.mobileconfig` file, ensuring macOS devices can seamlessly trust DoD-signed websites.
- **Easy Deployment**: Generates a downloadable `.mobileconfig` file, making it easy to distribute and deploy across macOS devices.

## Getting Started

### Prerequisites

- macOS device for testing and deployment
- Python 3.x installed on your system (for local script execution)
- Git installed on your system (for cloning the repository)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/dod.mobileconfig.git
   cd dod.mobileconfig
   ```

2. **(Optional) Run the script locally:** If you wish to manually run the script to generate the `.mobileconfig` file, ensure you have the required Python packages installed:

   ```bash
   pip install requests beautifulsoup4
   python process_certs.py
   ```

### Usage

The primary method of using this tool is through its automated GitHub Actions workflow, which runs daily to check for new certificates. However, you can manually trigger the workflow or run the script locally if needed.

To deploy the generated `.mobileconfig` file:

1. Download the latest `dod.mobileconfig` from the project's Releases page.
2. Distribute and install the `.mobileconfig` file on macOS devices as needed. This can typically be done via email, a web download, or through MDM (Mobile Device Management) solutions.
3. Once installed, you must go to `System Settings > Privacy & Security > Profiles`, double-click the profile, and install it.

## Contributing

Contributions to `dod.mobileconfig` are welcome! Please feel free to submit pull requests or open issues to discuss potential improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is not officially endorsed by or affiliated with the Department of Defense.