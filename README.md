
You can use this simple and powerful cli tool to access to the filescan service.

## Installation

```
      pip install filescan_cli
```

or

```      
      pip install -r requirements.txt
```

## Initial Configuration

In order to run CLI commands, you need to provide your API key and (optionally) webservice url.

The easiest way to provide the API key is to store it using the config command. Please generate an API key in your profile settings page (e.g. https://www.filescan.io/users/profile) and run the following command:

```
      python filescan.py config -x <API_KEY>
```

More information regarding the `config` command:
```
      python filescan.py config --help
```

## General Usage

```
      python filescan.py COMMAND [OPTIONS]
```

## Commands

-  `config`
  : Set global configurations

-  `upload`
  : Upload a file

-  `upload_link`
  : Upload a link

-  `export`
  : Export a report in the given format

-  `file`
  : Download a file

-  `report`
  : Get a report with report id and file hash

-  `scan_reports`
  : Get reports from a scan

-  `reports`
  : Get reports summary

-  `search`
  : Search reports

-  `sysconfig`
  : Get system configuration

-  `sysinfo`
  : Get system information

You can see detailed options by running the command with --help option

```
      filescan.py export --help
```

## Example CLI Output

<img src="https://user-images.githubusercontent.com/20181242/159781500-e59f6b57-e533-4f35-906a-f216a09620be.png" width="600">

## Alternative Configuration

You can pass a JSON config file using the `--config` option.

```
      python filescan.py --config ./config.json
```

Example JSON format:

```
      {
        "API_KEY": "cI3qhN1WewKw_JP_HiRiongypdZxg4TkJNiB-X22",
        "SERVICE_BASE_URL": "https://www.filescan.io"
      }
```

Alternatively, you can set environment variables

Unix:
```
      export API_KEY=cI3qhN1WewKw_JP_HiRiongypdZxg4TkJNiB-X22
      export SERVICE_BASE_URL=https://www.filescan.io
```

Windows:
```
      set API_KEY=cI3qhN1WewKw_JP_HiRiongypdZxg4TkJNiB-X22
      set SERVICE_BASE_URL=https://www.filescan.io
```
