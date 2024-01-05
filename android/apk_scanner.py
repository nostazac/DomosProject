from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm
from androguard.core.analysis import analysis

def scan_apk(file_path):
    # Load apk file
    a = apk.APK(file_path)
    
    #display basic information
    print("[+] Package Name:", a.get_package())
    print("[+] MainActivity:", a.get_main_activity())
    print("[+] Permissions: ", a.get_permissions())
    
    # Perform more in-depth analysis using androguard
    d = dvm.DalvikVMFromat(a.get_dex())
    dx = analysis.Analysis(d)
    
    # Display information about classes and methods
    print("\n[+] Classes: ")
    
    for clazz in d.get_classes():
        print("    -", clazz.get_name())
        
    print("\n[+] Methods: ") 
    for method in d.get_methods():
        print("     -", method.get_name())
if __name__ == "__main__":
    # Specify path to the APK file
    apk_path = "path/to/your/apk.apk"
    
    # Call the scan_apk function
    scan_apk(apk_path)