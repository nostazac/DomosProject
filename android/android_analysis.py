import frida
import sys

package_name = "com.example.targetapp"

frida_script = """

Java.perform(functioin () {
    //example:hooking a maethod in the target application
    var targetClass = Java.use("com.example.targetapp.TargetClass");
    targetClass.targetMethod,implementation = function () {
        console.log("[*] Intercepted targetMethod");
        //add your custom logic here or leave it empty for logging purposes
        return this.targrtMethod.apply(this, arguements);
    };
    
});

"""
def on_message(message, data):
    if "payload" in message:
        print(message["payload"])

def run_frida_script(package_name, script):
    
    try:
        # Attach target application
        process = frida.get_usb_device().attach(package_name)
        
        # Create a script from the provided Javascript
        
        script = process.create_script(script)
        
        
        # Setup message handler
        script.on("message", on_message)
        
        # Load the scripts into the target application
        
        script.load()
        
        # Keeo script running
        sys.stdin.read()
        
    except frida.ServerNotRunningError:
        print("{!} Frida serverid not running. please start the server.")
        
if __name__ == "__main__":
    run_frida_script(package_name, frida_script)