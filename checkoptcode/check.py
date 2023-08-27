import os
jitTests = ["3d-cube-SP", "3d-raytrace-SP", "acorn-wtb", "ai-astar", "Air", "async-fs", "Babylon", "babylon-wtb", "base64-SP", "Basic", "Box2D", "cdjs", "chai-wtb", "coffeescript-wtb", "crypto", "crypto-aes-SP", "crypto-md5-SP", "crypto-sha1-SP", "date-format-tofte-SP", "date-format-xparb-SP", "delta-blue", "earley-boyer", "espree-wtb", "first-inspector-code-load", "FlightPlanner", "float-mm.c", "gaussian-blur", "gbemu", "hash-map", "jshint-wtb",
            "json-parse-inspector", "json-stringify-inspector", "lebab-wtb", "mandreel", "ML", "multi-inspector-code-load", "n-body-SP", "navier-stokes", "octane-code-load", "octane-zlib", "OfflineAssembler", "pdfjs", "prepack-wtb", "raytrace", "regex-dna-SP", "regexp", "richards", "splay", "stanford-crypto-aes", "stanford-crypto-pbkdf2", "stanford-crypto-sha256", "string-unpack-code-SP", "tagcloud-SP", "typescript", "uglify-js-wtb", "UniPoker", "WSL"]

for test in jitTests:
    cmd = f"python3 checkoptcode.py ~/JetStream2/optcode/random/{test}.txt"
    os.system(cmd)
