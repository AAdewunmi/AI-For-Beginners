# דוגמאות ידידותיות למתחילים בבינה מלאכותית

ברוכים הבאים! תיקייה זו מכילה דוגמאות פשוטות ועצמאיות שיעזרו לכם להתחיל עם בינה מלאכותית ולמידת מכונה. כל דוגמה מעוצבת להיות ידידותית למתחילים עם הערות מפורטות והסברים שלב-אחר-שלב.

## 📚 סקירת דוגמאות

| דוגמה | תיאור | רמת קושי | דרישות מוקדמות |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | התוכנית הראשונה שלך בבינה מלאכותית - זיהוי תבניות פשוט | ⭐ מתחיל | יסודות פייתון |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | בניית רשת עצבית מהבסיס | ⭐⭐ מתחילים+ | פייתון, מתמטיקה בסיסית |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | סיווג תמונות עם מודל מאומן מראש | ⭐⭐ מתחילים+ | פייתון, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | ניתוח סנטימנט של טקסט (חיובי/שלילי) | ⭐⭐ מתחילים+ | פייתון |

## 🚀 התחלה

### דרישות מוקדמות

ודא שיש לך פייתון מותקן (מומלץ גרסה 3.8 ומעלה). התקן את החבילות הנדרשות:

```bash
# לסקריפטים של פייתון
pip install numpy

# למחברות ג'ופיטר (מסווג תמונות)
pip install jupyter numpy pillow tensorflow
```

או השתמש בסביבת conda מתוך תוכנית הלימודים הראשית:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### הרצת הדוגמאות

**לקבצי Python (.py):**
```bash
python 01-hello-ai-world.py
```

**לקבצי Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 מסלול לימוד

אנו ממליצים לעקוב אחר הדוגמאות לפי הסדר:

1. **התחל עם "Hello AI World"** - למד את יסודות זיהוי התבניות
2. **בנה רשת עצבית פשוטה** - הבן כיצד רשתות עצביות פועלות
3. **נסה את המסווג תמונות** - ראה בינה מלאכותית בפעולה עם תמונות אמיתיות
4. **נתח סנטימנט טקסט** - חקור עיבוד שפה טבעית

## 💡 טיפים למתחילים

- **קרא את ההערות בקוד בקפידה** - הן מסבירות מה כל שורה עושה
- **תנסה!** - נסה לשנות ערכים וראה מה קורה
- **אל תדאג אם לא תבין הכל מיד** - למידה לוקחת זמן
- **שאל שאלות** - השתמש בלוח הדיונים [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 שלבים הבאים

לאחר סיום דוגמאות אלו, חקור את תוכנית הלימודים המלאה:
- [מבוא לבינה מלאכותית](../lessons/1-Intro/README.md)
- [רשתות עצביות](../lessons/3-NeuralNetworks/README.md)
- [ראייה ממוחשבת](../lessons/4-ComputerVision/README.md)
- [עיבוד שפה טבעית](../lessons/5-NLP/README.md)

## 🤝 תרומה

מצאת את הדוגמאות האלה מועילות? עזור לנו לשפר אותן:
- דווח על בעיות או הצע שיפורים
- הוסף דוגמאות נוספות למתחילים
- שפר את התיעוד וההערות

---

*זכור: כל מומחה היה פעם מתחיל. לימודים מהנים! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->