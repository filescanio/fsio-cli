
You can use this simple and powerful cli tool to access to the filescan service.

## Installation

  `pip install filscan_cli`

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

## Configuration

In order to run the cli commands, you need to store your API key and (optionally) service url. There is multiple ways to do this (see 'Alternative Configuration' below for additional options).

In general, you can set the configuration values using the `config` command.
```
      python filescan.py config [OPTIONS]
```

Example using filescan.io as your default service endpoint:

```
      python filescan.py config -x <API_KEY>
```

## Example CLI Output

![image](https://user-images.githubusercontent.com/20181242/159781500-e59f6b57-e533-4f35-906a-f216a09620be.png)

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
