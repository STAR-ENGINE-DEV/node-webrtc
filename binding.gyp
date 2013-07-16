{
  'variables': {
    'mc%': 'lib/mozilla-central',
    'obj%': 'obj-x86_64-apple-darwin10.8.0'
  },
  'targets': [
    {
      'target_name': 'webrtc',
      'dependencies': [],
      'variables': {
      },
      'xcode_settings':{
        'OTHER_CFLAGS': [
                        '-std=gnu++0x',
                        '-Wno-c++0x-extensions',
                        '-Wno-c++11-extensions',
                        '-Wno-ignored-qualifiers',
                        '-Wno-invalid-offsetof'
        ]
      },
      'defines': [
      ],
      'include_dirs': [
	'<(mc)/media/webrtc/trunk/testing/gtest/include',
	'<(mc)/ipc/chromium/src',
	'<(mc)/media/mtransport',
	'<(mc)/media/mtransport/test',
	'<(mc)/media/webrtc/signaling/include',
	'<(mc)/media/webrtc/signaling/src/sipcc/core/sdp',
	'<(mc)/media/webrtc/signaling/src/sipcc/cpr/include',
	'<(mc)/media/webrtc/signaling/src/sipcc/core/includes',
	'<(mc)/media/webrtc/signaling/src/common/browser_logging',
	'<(mc)/media/webrtc/signaling/src/media',
	'<(mc)/media/webrtc/signaling/src/media-conduit',
	'<(mc)/media/webrtc/signaling/src/mediapipeline',
	'<(mc)/media/webrtc/signaling/src/sipcc/include',
	'<(mc)/media/webrtc/signaling/src/peerconnection',
	'<(mc)/media/webrtc/signaling/media-conduit',
	'<(mc)/media/webrtc/trunk/third_party/libjingle/source/',
	'<(mc)/xpcom/base/',
	'<(mc)/media/webrtc/trunk/webrtc',
	'<(mc)/ipc/chromium/src',
	'<(mc)/ipc/glue',
	'<(mc)/media/webrtc/signaling/test',
	'<(mc)/<(obj)/dist/include/nspr',
	'<(mc)/<(obj)/dist/include/nss',
	'<(mc)/<(obj)/dist/include',
	'<(mc)/<(obj)/dist/include/testing',
      ],
      'link_settings': {
        'ldflags': [
        ],
        'libraries': [
          '../<(mc)/<(obj)/dist/lib/XUL',
          '../<(mc)/<(obj)/dist/lib/libmozalloc.dylib',
          '../<(mc)/<(obj)/dist/lib/libnspr4.a',
          '../<(mc)/<(obj)/dist/lib/libplc4.a',
          '../<(mc)/<(obj)/dist/lib/libplds4.a',
          '../<(mc)/<(obj)/dist/lib/libcrmf.a',
          '../<(mc)/<(obj)/dist/lib/libsmime3.dylib',
          '../<(mc)/<(obj)/dist/lib/libssl3.dylib',
          '../<(mc)/<(obj)/dist/lib/libnss3.dylib',
          '../<(mc)/<(obj)/dist/lib/libnssutil3.dylib',
          '../<(mc)/<(obj)/dist/lib/libxpcomglue_s.a',
          '../<(mc)/<(obj)/dist/lib/libmtransport_s.a',
          '../<(mc)/<(obj)/dist/lib/libecc.a',
          '../<(mc)/<(obj)/dist/lib/libsipcc.a',
	'../<(mc)/<(obj)/dist/lib/libmozots.a',
	'../<(mc)/<(obj)/dist/lib/libmozqcms.a',
	'../<(mc)/<(obj)/dist/lib/libmozgraphite2.a',
	'../<(mc)/<(obj)/dist/lib/libmozharfbuzz.a',
	'../<(mc)/<(obj)/dist/lib/libmozcairo.a',
	'../<(mc)/<(obj)/dist/lib/libmozlibpixman.a',
	'../<(mc)/<(obj)/dist/lib/libvorbis.a',
	'../<(mc)/<(obj)/dist/lib/libogg.a',
	'../<(mc)/<(obj)/dist/lib/libtheora.a',
	'../<(mc)/<(obj)/dist/lib/libopus.a',
	'../<(mc)/<(obj)/dist/lib/libnestegg.a',
	'../<(mc)/<(obj)/dist/lib/libvpx.a',
	'../<(mc)/<(obj)/dist/lib/libspeex_resampler.a',
	'../<(mc)/<(obj)/dist/lib/libsoundtouch.a',
	'../<(mc)/<(obj)/dist/lib/libcubeb.a',
	'../<(mc)/<(obj)/dist/lib/libmozpng.a',
	'../<(mc)/<(obj)/dist/lib/libmozjpeg.a',
	'../<(mc)/<(obj)/dist/lib/libangle.a',
	'../<(mc)/<(obj)/dist/lib/libmozexpat_s.a',
	'../<(mc)/<(obj)/dist/lib/libgfx2d.a',
	'../<(mc)/<(obj)/dist/lib/libskia.a',
	'../<(mc)/<(obj)/dist/lib/libwebvtt.a',
	'../<(mc)/<(obj)/dist/lib/libcommon_video.a',
	'../<(mc)/<(obj)/dist/lib/libvideo_capture_module.a',
	'../<(mc)/<(obj)/dist/lib/libwebrtc_utility.a',
	'../<(mc)/<(obj)/dist/lib/libaudio_coding_module.a',
	'../<(mc)/<(obj)/dist/lib/libCNG.a',
	'../<(mc)/<(obj)/dist/lib/libsignal_processing.a',
	'../<(mc)/<(obj)/dist/lib/libG711.a',
	'../<(mc)/<(obj)/dist/lib/libPCM16B.a',
	'../<(mc)/<(obj)/dist/lib/libNetEq.a',
	'../<(mc)/<(obj)/dist/lib/libresampler.a',
	'../<(mc)/<(obj)/dist/lib/libvad.a',
	'../<(mc)/<(obj)/dist/lib/libsystem_wrappers.a',
	'../<(mc)/<(obj)/dist/lib/libwebrtc_video_coding.a',
	'../<(mc)/<(obj)/dist/lib/libwebrtc_i420.a',
	'../<(mc)/<(obj)/dist/lib/libwebrtc_vp8.a',
	'../<(mc)/<(obj)/dist/lib/libwebrtc_opus.a',
	'../<(mc)/<(obj)/dist/lib/libvideo_render_module.a',
	'../<(mc)/<(obj)/dist/lib/libvideo_engine_core.a',
	'../<(mc)/<(obj)/dist/lib/libmedia_file.a',
	'../<(mc)/<(obj)/dist/lib/librtp_rtcp.a',
	'../<(mc)/<(obj)/dist/lib/libudp_transport.a',
	'../<(mc)/<(obj)/dist/lib/libbitrate_controller.a',
	'../<(mc)/<(obj)/dist/lib/libremote_bitrate_estimator.a',
	'../<(mc)/<(obj)/dist/lib/libpaced_sender.a',
	'../<(mc)/<(obj)/dist/lib/libvideo_processing.a',
	'../<(mc)/<(obj)/dist/lib/libvoice_engine_core.a',
	'../<(mc)/<(obj)/dist/lib/libaudio_conference_mixer.a',
	'../<(mc)/<(obj)/dist/lib/libaudio_device.a',
	'../<(mc)/<(obj)/dist/lib/libaudio_processing.a',
	'../<(mc)/<(obj)/dist/lib/libyuv.a',
	'../<(mc)/<(obj)/dist/lib/libnicer.a',
	'../<(mc)/<(obj)/dist/lib/libnrappkit.a',
	'../<(mc)/<(obj)/dist/lib/libvideo_processing_sse2.a',
	'../<(mc)/<(obj)/dist/lib/libaudio_processing_sse2.a',
        '../<(mc)/<(obj)/dist/lib/libnksctp_s.a',
#	-framework AudioToolbox
#	-framework
#	AudioUnit
#	-framework
#	Carbon
#	-framework
#	CoreAudio
#	-framework
#	OpenGL
#	-framework
#	QTKit
#	-framework
#	QuartzCore
#	-framework
#	Security
#	-framework
#	SystemConfiguration
#	-framework
#	IOKit
#	-F/System/Library/PrivateFrameworks
#	-framework
#	CoreUI
#	-framework
#	CoreLocation
#	-framework
#	QuartzCore
#	-framework
#	Carbon
#	-framework
#	CoreAudio
#	-framework
#	AudioToolbox
#	-framework
#	AudioUnit
#	-framework
#	AddressBook
#	-framework
#	OpenGL
        ]
      },
      'sources': [
        'src/binding.cc',
        'src/peerconnection.cc',
      # 'src/create-session-description-observer.cc',
      # 'src/set-remote-description-observer.cc'
      ]
    }
  ]
}
