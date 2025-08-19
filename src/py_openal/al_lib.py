from .library_loader import ExternalLibrary, ExternalLibraryError

lib = None
for name in ("soft_oal", "OpenAL32", "openal"):
    try:
        lib = ExternalLibrary.load(name)
    except:
        continue
    if lib: break

if not lib:
    raise ExternalLibraryError("OpenAL library couldn't be found")
