# ကုဒ်ကို run လုပ်နည်း

ဒီသင်ရိုးတွင် run လုပ်လိုစိတ်ရှိမယ့် executable ဥပမာနဲ့ စမ်းသပ်မှုတွေ များပြားနေပါတယ်။ ဒါကိုလုပ်ဖို့အတွက်, သင်ရိုးအချက်အချာတွင်ပါဝင်တဲ့ Jupyter Notebooks ဂြိုဟ်တွင် Python ကုဒ်ကို run လုပ်နိုင်စွမ်းလိုအပ်ပါတယ်။ Run လုပ်ရာမှာတော့ ရွေးချယ်စရာစုံရှိပါတယ်။

## ကိုယ့်ကွန်ပျူတာပေါ်မှာ locally run လုပ်ခြင်း

ကိုယ့်ကွန်ပျူတာပေါ်မှာ locally run လုပ်ဖို့ Python installation လိုအပ်ပါတယ်။ တစ်ခုအကြံပြုချင်တာက **[miniconda](https://conda.io/en/latest/miniconda.html)** ကို install လုပ်တာပါ - ဒါက လွယ်ကူဘဲ 설치 ဖြစ်ပြီး Python နဲ့အမျိုးမျိုးသော **virtual environments** အတွက် `conda` package manager ကို support လုပ်ပါတယ်။

miniconda install လုပ်ပြီးတဲ့နောက်, repository ကို clone လုပ်ပြီး သင်တန်းအတွက် အသုံးပြုမယ့် virtual environment တစ်ခုကို တည်ဆောက်ပါ။

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code ကို Python Extension နှင့် သုံးခြင်း

ဒီသင်ရိုးကို အကောင်းဆုံးအသုံးပြုဖို့အတွက် [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ကို [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) နဲ့ကောင်းကောင်းဖွင့်သုံးပါ။

> **မှတ်ချက်**: repository ကို clone လုပ်ပြီး VS Code မှာဖွင့်မယ်ဆိုရင် Python extensions ကို install လုပ်ဖို့ အလိုအလျောက် sugesst လုပ်ပါလိမ့်မယ်။ အထက်ဖေါ်ပြခဲ့တဲ့အတိုင်း miniconda ကိုလည်း install လုပ်ထားဖို့လိုပါပဲ။

> **မှတ်ချက်**: VS Code က repository ကို container တစ်ခုအဖြစ်ပြန်ဖွင့်ဖို့ sugesst လုပ်လာရင် local Python installation သုံးဖို့ အဲ့ဒီတောင်းဆိုမှုကို ပယ်ချသင့်ပါတယ်။

### Browser မှ Jupyter သုံးခြင်း

ကိုယ့်ကိုယ်ပိုင်ကွန်ပျူတာပေါ်မှာ browser ကနေ Jupyter environment ကိုသုံးနိုင်ပါတယ်။ classic Jupyter နဲ့ JupyterHub ဖွင့်တဲ့အခါမှာ auto-completion, code highlighting စတာတွေပါဝင်တဲ့ ထောက်ပံ့ရေးကောင်းတဲ့ဖွံ့ဖြိုးရေး အခြေအနေကိုရရှိပါတယ်။

Jupyter ကို locally စလိုချင်ရင် သင်တန်းဖိုင်ရှိတဲ့ directory ကို သွားပြီး အောက်ပါ command ကို run လုပ်ပါ -

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
ပြီးရင် `.ipynb` ဖိုင်တွေကိုရွေးပြီးဖွင့်နိုင်ပါပြီ၊ မိမိလုပ်ဆောင်စတင်နိုင်ပါပြီ။

### Container ထဲမှာ run လုပ်ခြင်း

Python installation အစား container ထဲ run လုပ်နိုင်ပါတယ်။ ကျွန်တော်တို့ repo မှာ `.devcontainer` ဆိုတဲ့ folder တစ်ခု ထည့်ထားပြီး container ပြုပြင်ဖွဲ့စည်းနည်း ဖော်ပြပေးထားတာကြောင့် VS Code မှာ container အဖြစ် အလွယ်တကူဖွင့်စီမံရန် အခွင့်အရေးပေးပါတယ်။ ဒါအတွက် Docker installation လိုအပ်ပြီး အနည်းငယ်ရှုပ်ထွေးတာကြောင့် အတွေ့အကြုံရှိသူတွေကို အကြံပြုပါတယ်။

## Cloud မှာ run လုပ်ခြင်း

Python ကို ကိုယ့်ကွန်ပျူတာမှာ install မလုပ်ချင်ဘူးဆိုရင်နဲ့ cloud resource တွေကိုအသုံးချနိုင်တယ်ဆိုရင် cloud မှာ run လုပ်ရတာကောင်းသောရွေးချယ်စရာတခုဖြစ်ပါတယ်။ တွဲချိတ် run လုပ်နည်းအများအပြားရှိတယ် -

* **[GitHub Codespaces](https://github.com/features/codespaces)** ကိုသုံးခြင်း - GitHub ပေါ်မှာ virtual environment တစ်ခု ဖန်တီးပေးပြီး VS Code browser interface ကနေ ဝင်ရောက် အသုံးပြုနိုင်ပါတယ်။ Codespaces ကိုရနိုင်သူဆိုရင် repo မှာ **Code** ခလုတ်ကိုနှိပ်ပြီး codespace ကို စတင်၍ အချိန်မကုန် run လုပ်လို့ရပါတယ်။
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** ကိုသုံးခြင်း။ [Binder](https://mybinder.org) က GitHub အတွက် cloud ပေါ်က ဝေစုစရင်းလွတ်လပ်သော computing resource ကို ပေးသည်။ Repo ကို Binder နှင့်ဖွင့်ရန် အရင်စာမျက်နှာမှာ ခလုတ်ရှိပြီး အဲ့ဒီနေရာကို ဦးတည်သွားသလို container တည်ဆောက်ပြီး Jupyter web interface ကို မည်သည့်အဆင်ပြေလွယ်ကူစွာ စတင်ပေးပါမယ်။

> **မှတ်ချက်**: မမှန်ကန်သင့်စွဲမှုများကို ကာကွယ်ရန် Binder မှ အချို့ web resource များကို ပိတ်ထားသည်။ ဒါက model များနဲ့ ဒေတာကို ပြင်ပ အင်တာနက်မှ ရယူတဲ့ ကုဒ်များ အလုပ်မလုပ်ပဲရပ်တန့်နိုင်သလို အခြားနည်းလမ်းရှာဖွေရန် လိုအပ်နိုင်ပါတယ်။ ထို့အပြင် Binder ကပေးတဲ့ တိုက္ခိုက်မှု resource များမကြာခဏမလုံလောက်ကြောင်းကြောင့် စိတ်ဝင်စားဖွယ် training တွေ အထူးသဖြင့် နောက်ပိုင်း ရှုပ်ထွေးတဲ့ သင်ခန်းစာတွင် နှေးကွေးတတ်ပါတယ်။

## GPU ပါရှိသည့် Cloud မှာ run လုပ်ခြင်း

ဒီသင်ရိုးအချို့ နောက်ပိုင်းသင်ခန်းစာများအတွက် GPU support ရှိဖို့ အရေးကြီးပါတယ်။ နမူနာအတွက် model training က မဖြစ်မနေမြန်ကာတတ်ပါတယ်။ cloud ကို အသုံးပြုခြင်းအထူးသဖြင့် [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) သို့မဟုတ် သင်တန်းတက်နေလို့ ရနိုင်တဲ့ အဖွဲ့အစည်းမှ cloud ကို မှတ်ပုံတင်ထားပြီးပိုမိုကောင်းမွန်သော အစီအစဉ်များအတွက် အောက်ပါနည်းလမ်းများ ရှိပါတယ်။

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) တစ်ခု ဖန်တီးပြီး Jupyter နဲ့ချိတ်ဆက်ပါ။ အဲဒီအခြေအနေမှာ repo ကို တိုက်ရိုက် machine ထဲ clone လုပ်ပြီး သင်ယူစတင်နိုင်ပါတယ်။ NC-series VM များတွင် GPU support ပါဝင်သည်။

> **မှတ်ချက်**: Azure for Students အပါအဝင် အချို့ subscription များတွင် GPU support ကို ပူးတွဲပေးခြင်း မရှိနိုင်ပါ။ အပို GPU core များရရန် နည်းပညာဆိုင်ရာ မေးခွန်းတင်ရန် လိုအပ်တတ်ပါသည်။

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) တည်ဆောက်ပြီး အဲဒီမှာ Notebook အပြင်ဆင်ချက်ကို အသုံးပြုနိုင်သည်။ [ဒီဗွီဒီယို](https://azure-for-academics.github.io/quickstart/azureml-papers/) မှာ Azure ML notebook တွင် repository ကို clone လုပ်ပြီး သုံးပုံပြပေးထားပါတယ်။

Google Colab ကိုလည်း အသုံးပြုနိုင်ပြီး ဒါဟာ အခမဲ့ GPU မှာရှိ၊ Jupyter Notebooks ကို တစ်ခါတိုင်းတင်ပြီး run လုပ်နိုင်ပါတယ်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->