<!--

classDiagram
class hero{
 *INTEGER id NOT NULL
   INTEGER age
   VARCHAR name NOT NULL
   VARCHAR secret_name NOT NULL
   INTEGER team_id
}
class heromissionlink{
 *INTEGER hero_id NOT NULL
   *INTEGER mission_id NOT NULL
}
class mission{
 *INTEGER id NOT NULL
   VARCHAR description NOT NULL
   VARCHAR name NOT NULL
}
class team{
 *INTEGER id NOT NULL
   VARCHAR headquarters NOT NULL
   VARCHAR name NOT NULL
}
team "0..1" -- "0..n" hero
hero "1" -- "0..n" heromissionlink
mission "1" -- "0..n" heromissionlink

-->
![](https://mermaid.ink/img/Y2xhc3NEaWFncmFtCmNsYXNzIGhlcm97CiAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBJTlRFR0VSIGFnZQogICBWQVJDSEFSIG5hbWUgTk9UIE5VTEwKICAgVkFSQ0hBUiBzZWNyZXRfbmFtZSBOT1QgTlVMTAogICBJTlRFR0VSIHRlYW1faWQKfQpjbGFzcyBoZXJvbWlzc2lvbmxpbmt7CiAqSU5URUdFUiBoZXJvX2lkIE5PVCBOVUxMCiAgICpJTlRFR0VSIG1pc3Npb25faWQgTk9UIE5VTEwKfQpjbGFzcyBtaXNzaW9uewogKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVkFSQ0hBUiBkZXNjcmlwdGlvbiBOT1QgTlVMTAogICBWQVJDSEFSIG5hbWUgTk9UIE5VTEwKfQpjbGFzcyB0ZWFtewogKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVkFSQ0hBUiBoZWFkcXVhcnRlcnMgTk9UIE5VTEwKICAgVkFSQ0hBUiBuYW1lIE5PVCBOVUxMCn0KdGVhbSAiMC4uMSIgLS0gIjAuLm4iIGhlcm8KaGVybyAiMSIgLS0gIjAuLm4iIGhlcm9taXNzaW9ubGluawptaXNzaW9uICIxIiAtLSAiMC4ubiIgaGVyb21pc3Npb25saW5r)
