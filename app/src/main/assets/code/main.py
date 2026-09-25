import os
import zipfile
import sys

def decompile_apk_python(apk_path, output_dir):
    print("=" * 60)
    print("   أداة تفكيك التطبيقات بلغة بايثون (Python APK Unpacker)   ")
    print("=" * 60)

    # 1. التأكد من وجود ملف الـ APK
    if not os.path.exists(apk_path):
        print(f"❌ خطأ: الملف [{apk_path}] غير موجود!")
        return

    # 2. إنشاء مجلد الحفظ
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 تم إنشاء مجلد الحفظ: {output_dir}")

    try:
        print("\n⏳ جاري فك ضغط ملف الـ APK واستخراج المحتويات...")
        
        # ملف الـ APK هو في الأصل ملف مضغوط Zip
        with zipfile.ZipFile(apk_path, 'r') as apk_zip:
            apk_zip.extractall(output_dir)
            
        print("✅ تم استخراج كافة ملفات التطبيق بنجاح!")
        print("-" * 50)
        
        # استعراض أهم الملفات المستخرجة
        print("📂 أهم الملفات والأكواد التي تم استخراجها:")
        extracted_files = os.listdir(output_dir)
        
        for item in extracted_files:
            if item.endswith('.dex'):
                print(f"  📄 ملف كود برمجية (DEX Executable): {item}")
            elif item == 'AndroidManifest.xml':
                print(f"  📜 ملف المانفيست (Manifest Config): {item}")
            elif item == 'res':
                print(f"  🖼️ مجلد الموارد والواجهات (Resources): {item}/")
            elif item == 'assets':
                print(f"  📦 مجلد الأصول والملفات الإضافية (Assets): {item}/")
                
        print("-" * 50)
        print(f"🎯 يمكنك الآن فتح المجلد [{output_dir}] وتصفح الأكواد والملفات.")

    except Exception as e:
        print(f"\n❌ حدث خطأ أثناء فك التفكيك: {str(e)}")

if __name__ == "__main__":
    # أدخل مسار ملف الـ APK الخاص بك هنا
    print("أهلاً بك! يرجى إدخال اسم أو مسار ملف الـ APK:")
    input_file = input("مسار الملف (مثال: myapp.apk): ").strip()
    
    output_folder = "APK_Decompiled_Result"
    
    if input_file:
        decompile_apk_python(input_file, output_folder)
    else:
        print("❌ لم يتم إدخال مسار الملف!")
