{
	# This file should contain any project specific configuration / applications
	# All xcode config files should be agile between projects
	# should be primarily responsible for any user-changing elements 
	# ie: frameworks, provisioning profile, output paths etc

	# initialize global variables as needed for application
	'variables' : {

		# sdk version of application being used
		'ios_sdk_version': '7.0',

		# sdk directory that we are currently using
		'ios_sdk_dir': '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS',

		'plist_file': 'Aizel/Info.plist',

		'build_directory': '<!(pwd)/build',
		
		'scripts_dir': 'scripts'
	},

	# global conditions for application
	'target_defaults' : {

		'xcode_settings' : {

			'SDKROOT': 'iphoneos',
			'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
			'OTHER_CFLAGS': ['-fobjc-arc'],
			'INFOPLIST_FILE' : '<(plist_file)',
			#'ARCHS': '$(ARCHS_STANDARD)',			
			'PRODUCT_NAME': 'Aizel',
			#'HEADER_SEARCH_PATHS': '$(inherited) src',
		},

		'link_settings': {

			'libraries': [

				'$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
				'$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
				'$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
				'$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
			],
		},

		'type': 'executable',
		'mac_bundle': 1,

		'include_dirs' : [

			'Aizel'
		],

		# now go ahead and grab all of the correct source files for this application and insert them here
		'sources': [

			'<!@(find Aizel -type f \( -name \'*.m\' -o -name \'*.h\' -o -name \'*.plist\' \))'
			
		],

		'mac_bundle_resources': [
			'<!@(find Aizel -type f \( -name \'*.storyboard\' -o -name \'*.xib\' -o -name \'*.xcasset\' \))'
		],

	}, # GLOBAL CONDITIONS ETC

	'xcode_config_file': 'config/shared.xcconfig',

	# Schemes are user derived for running targets once they are built -- we don't want this as we want all developers to be able to run this automatically
	# targets = ['debug', 'test', 'release']
	'targets': [

		# debug is for device testing as well as general development testing
		# this can also be updated to testflight as well
		{
			'target_name': 'Aizel',
      			'product_name': 'Aizel',
      			'xcode_config_file': './config/debug.xcconfig',
			
			'postbuilds': [

				{
					'postbuild_name': 'test',
					'action': ['/bin/bash', '<(scripts_dir)/test.sh'], 
				}
			],
		},
	]# end of all targets
}
