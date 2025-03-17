# Rule 240.15-la-ii doc repository

## Cases

- Source: https://www.finra.org/rules-guidance/key-topics/regulation-best-interest#enforcement
- Retrieval: ./scripts/retrieve-cases.sh
- PDF destination: ./casespdfs/{case-number}
- Txt destination: ./casestxt/{case-number}
- Summaries from Claude: ./cases_summaries/{case-number}


## Claude Desktop (Mac Only)

- Download Claude Desktop.  
- Edit claude_desktop_config: Claude->Settings->Developer->Edit Config.
``` 
{
  "mcpServers": {
    "brave-search": {
      "command":"/Users/fettermania/.nvm/versions/node/v22.14.0/bin/npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "YOUR_KEY_HERE"
      }
    },
    "github": {
      "command":"/Users/fettermania/.nvm/versions/node/v22.14.0/bin/npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_KEY_HERE"
      }
    },
   "sequential-thinking": {
      "command":"/Users/fettermania/.nvm/versions/node/v22.14.0/bin/npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
  "fetch": {
    "command": "uvx",
    "args": ["mcp-server-fetch", "--ignore-robots-txt"]
  },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/fettermania/Desktop/claude"
      ]
    }
  }
  ```
- Note: Lines should be your own installations destinations of node.  
- Note: Only two required ones are 'fetch' and 'filesystem'.  
- Fetch extension config: 
  - Instructions: https://4sysops.com/archives/install-mcp-server-fetch-for-claude-ai-on-mac-and-windows/
- Filesystem extension config:
  - Instructions: https://mcp.so/server/filesystem
  - Note: The last line of the 'filesystem' config is a location on your machine that Claude is allowed to access.  Work from there.

  ## Claude Desktop (Windows)

  - The whole idea should work on Windows too but the configuration and downloads are different.  I don't have a windows machine.  Instructions of the extensions (MCP Servers) at the MCP websites also typically include a Windows version.

  ## Claude prompts

  - In prompts directory.  Update to your file path.  