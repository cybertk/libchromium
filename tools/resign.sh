#!/bin/sh

# [1][http://stackoverflow.com/questions/6896029/re-sign-ipa-iphone]

CODE_SIGN_IDENTITY='iPhone Distribution: Thomas Sachson'
PROVISIONING_PROFILE='/Users/quanlong/projects/origin_pa/src/tools/ios_dev_group7.mobileprovision'

IPA=$1

# Unzip the IPA
unzip $IPA

APP=$(ls -d Payload/*.app)
# Remove old CodeSignature, we don't have CodeResources
rm -rf "$APP/_CodeSignature"

# Replace embedded mobile provisioning profile
cp "$PROVISIONING_PROFILE" "$APP/embedded.mobileprovision"

# Re-sign, Removed the Entitlement part (see alleys comment, thanks)
codesign -f -s "$CODE_SIGN_IDENTITY" --resource-rules "$APP/ResourceRules.plist" "$APP"

# Re-package
zip -qr "${IPA%%.ipa}.resigned.ipa" Payload
