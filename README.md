
You can use this simple and powerful cli tool to access to the filescan service.

## Usage
  
  `python filescan.py [OPTIONS] COMMAND`

## Commands

-  `upload`
  : Upload a file

-  `export`
  : Export a report in the given format

-  `file`
  : Download a file

-  `report`
  : Get a report or reports from a scan

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
      python filescan.py export --help
```

## Configuration

In order to run the cli commands, you need to set the api key and service url to access. There are two options.

1. You can set the environment variables

```
      export API_KEY=123495594`
      export SERVICE_BASE_URL=123495594`
```
2. You can pass the config file path with `--config` option to the command. The config file should be in json format.

```
      python filescan.py --config ./config.json
```

Example json format

```
      {
        "API_KEY": "abcdefghiji",
        "SERVICE_BASE_URL": "http://staging.filescan.io"
      }
```

  
