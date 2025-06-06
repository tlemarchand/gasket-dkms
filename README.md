# gasket-dkms
![Build Status](https://copr.fedorainfracloud.org/coprs/kylegospo/google-coral-dkms/package/gasket-dkms/status_image/last_build.png?)

The Coral Gasket Driver allows usage of the [Coral EdgeTPU](https://coral.ai/) on Linux systems. The driver contains two modules:

* Gasket: Gasket (Google ASIC Software, Kernel Extensions, and Tools) is a top level driver for lightweight communication with Google ASICs.
* Apex: Apex refers to the [EdgeTPU v1](https://coral.ai/technology)

Includes necessary fix to run on 6.12 kernels (Fedora 41 and 42).

## Installing

You can get releases for Fedora, RHEL, CentOS, OpenSUSE, and OpenMandriva from my [Copr](https://copr.fedorainfracloud.org/coprs/tlemarchand/google-coral-dkms/).

If you wish to use this with Secure Boot, follow [this guide](https://gist.github.com/KyleGospo/9adbe078d1d7f160ae43c091df98f773).
