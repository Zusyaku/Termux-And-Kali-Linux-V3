#!/usr/bin/bash
#FellFreeToRecode
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
BlueF='\e[1;34m'
clear
BANNERS () {
printf "${lightgreen}==============================
         Nakanosec Tools
        h1 In Scope Grabber
${white}         -Nakanosec.com-${lightgreen}
==============================\n
"
}
BANNERS

OPTIONS () {
printf "${white}[${lightgreen}>${white}] ${lightgreen}USERNAME TARGET${white} (ex: https://hackerone.com/${lightgreen}grab${white}) :${lightgreen} "
read nama
}
OPTIONS
curl=$(curl -kls -X POST -H "Content-Type: application/json" -d '{"operationName":"TeamAssets","variables":{"handle":"'$nama'"},"query":"query TeamAssets($handle: String!) {\n  me {\n    id\n    membership(team_handle: $handle) {\n      id\n      permissions\n      __typename\n    }\n    __typename\n  }\n  team(handle: $handle) {\n    id\n    handle\n    structured_scope_versions(archived: false) {\n      max_updated_at\n      __typename\n    }\n    in_scope_assets: structured_scopes(first: 500, archived: false, eligible_for_submission: true) {\n      edges {\n        node {\n          id\n          asset_type\n          asset_identifier\n          rendered_instruction\n          max_severity\n          eligible_for_bounty\n          labels(first: 100) {\n            edges {\n              node {\n                id\n                name\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    out_scope_assets: structured_scopes(first: 500, archived: false, eligible_for_submission: false) {\n      edges {\n        node {\n          id\n          asset_type\n          asset_identifier\n          rendered_instruction\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}' "https://hackerone.com/graphql" | jq '.data .team .in_scope_assets .edges' |  grep -Po '"asset_identifier"\K.*?(?=,)' | sed 's|[": ]||g' > temp.txt);
printf "${white}[${lightgreen}+${white}]${lightgreen} Result${white}\n"
cat temp.txt
printf "${white}[${lightgreen}+${white}]${lightgreen} Done${white} \n"