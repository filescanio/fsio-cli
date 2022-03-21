
You can use this simple and powerful cli tool to access to the filescan service.

## Installation

  `pip install filscan_cli`

## Usage

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

## Configuration

In order to run the cli commands, you need to set the api key and service url to access. There are three options.

1. You can set the environment variables

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

2. You can pass the config file path with `--config` option to the command. The config file should be in json format.

```
      python filescan.py --config ./config.json
```

Example json format

```
      {
        "API_KEY": "cI3qhN1WewKw_JP_HiRiongypdZxg4TkJNiB-X22",
        "SERVICE_BASE_URL": "https://www.filescan.io"
      }
```

3. You can set the configuration values using `config` command.
```
      python filescan.py config [OPTIONS]
```

You can see detailed options by running the command with --help option
