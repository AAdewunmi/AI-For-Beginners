# ตัวอย่าง AI ที่เหมาะสำหรับผู้เริ่มต้น

ยินดีต้อนรับ! โฟลเดอร์นี้ประกอบด้วยตัวอย่างง่ายๆ ที่เป็นอิสระเพื่อช่วยให้คุณเริ่มต้นกับ AI และการเรียนรู้ของเครื่อง แต่ละตัวอย่างถูกออกแบบให้ง่ายสำหรับผู้เริ่มต้น โดยมีคำอธิบายและคำอธิบายทีละขั้นตอนอย่างละเอียด

## 📚 ภาพรวมตัวอย่าง

| Example | Description | Difficulty | Prerequisites |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | โปรแกรม AI แรกของคุณ - การจดจำรูปแบบง่ายๆ | ⭐ Beginner | พื้นฐาน Python |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | สร้างโครงข่ายประสาทเทียมจากศูนย์ | ⭐⭐ Beginner+ | Python, คณิตศาสตร์พื้นฐาน |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | จัดหมวดหมู่ภาพด้วยโมเดลที่ผ่านการฝึกมาแล้ว | ⭐⭐ Beginner+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | วิเคราะห์อารมณ์ข้อความ (บวก/ลบ) | ⭐⭐ Beginner+ | Python |

## 🚀 เริ่มต้นใช้งาน

### สิ่งที่ต้องเตรียม

ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Python แล้ว (แนะนำเวอร์ชัน 3.8 หรือสูงกว่า) ติดตั้งแพ็กเกจที่จำเป็น:

```bash
# สำหรับสคริปต์ Python
pip install numpy

# สำหรับโน้ตบุ๊ก Jupyter (ตัวจำแนกรูปภาพ)
pip install jupyter numpy pillow tensorflow
```

หรือใช้สภาพแวดล้อม conda จากหลักสูตรหลัก:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### การรันตัวอย่าง

**สำหรับสคริปต์ Python (.py files):**
```bash
python 01-hello-ai-world.py
```

**สำหรับโน้ตบุ๊ก Jupyter (.ipynb files):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 เส้นทางการเรียนรู้

เราแนะนำให้ทำตามตัวอย่างตามลำดับ:

1. **เริ่มต้นด้วย "Hello AI World"** - เรียนรู้พื้นฐานการจดจำรูปแบบ
2. **สร้างโครงข่ายประสาทเทียมง่ายๆ** - เข้าใจว่าโครงข่ายประสาททำงานอย่างไร
3. **ลองใช้ Image Classifier** - ดู AI ทำงานกับภาพจริง
4. **วิเคราะห์อารมณ์ข้อความ** - สำรวจการประมวลผลภาษาธรรมชาติ

## 💡 เคล็ดลับสำหรับผู้เริ่มต้น

- **อ่านคำอธิบายโค้ดอย่างละเอียด** - เพื่ออธิบายแต่ละบรรทัดว่าทำอะไร
- **ทดลอง!** - ลองเปลี่ยนค่าแล้วดูผลลัพธ์
- **อย่ากังวลถ้าไม่เข้าใจทุกอย่าง** - การเรียนรู้ต้องใช้เวลา
- **ถามคำถาม** - ใช้ [กระดานสนทนา](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 ขั้นตอนถัดไป

หลังจากทำตัวอย่างเหล่านี้เสร็จแล้ว ให้สำรวจหลักสูตรเต็ม:
- [แนะนำ AI](../lessons/1-Intro/README.md)
- [โครงข่ายประสาทเทียม](../lessons/3-NeuralNetworks/README.md)
- [วิสัยทัศน์คอมพิวเตอร์](../lessons/4-ComputerVision/README.md)
- [การประมวลผลภาษาธรรมชาติ](../lessons/5-NLP/README.md)

## 🤝 การมีส่วนร่วม

พบว่าตัวอย่างเหล่านี้มีประโยชน์? ช่วยเราปรับปรุง:
- รายงานปัญหาหรือแนะนำการปรับปรุง
- เพิ่มตัวอย่างเพิ่มเติมสำหรับผู้เริ่มต้น
- ปรับปรุงเอกสารและคำอธิบาย

---

*จำไว้ว่า: ผู้เชี่ยวชาญทุกคนเคยเป็นผู้เริ่มต้นมาก่อน ขอให้เรียนรู้อย่างมีความสุข! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->