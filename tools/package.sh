APP='/Users/quanlong/projects/origin_pa/src/xcodebuild/Release-iphoneos/Dev_quanlong.app'

IPA='/Users/quanlong/Desktop/x.ipa'
PROVISIONING_PROFILE='/Users/quanlong/projects/origin_pa/src/tools/ios_dev_group7.mobileprovision'

xcrun --sdk iphoneos PackageApplication "$APP" \
        -o "$IPA"
