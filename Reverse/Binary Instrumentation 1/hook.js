Interceptor.attach(Module.findExportByName("msvcrt.dll", "strcmp"), {
    onEnter(args) {
        console.log("strcmp called:");
        console.log("arg1: " + Memory.readUtf8String(args[0]));
        console.log("arg2: " + Memory.readUtf8String(args[1]));
    }
});
