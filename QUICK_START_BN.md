# Tour Money — iPhone-এ চালানোর সহজ নিয়ম

এটি একটি **ফ্রি Offline PWA**। ZIP ফাইল থেকে iPhone-এ সরাসরি `.html` খুলে স্থায়ী Offline App হিসেবে ইনস্টল হবে না। প্রথমে পুরো ফোল্ডারটি HTTPS ওয়েবসাইটে প্রকাশ করতে হবে। অ্যাপ প্রকাশ করার জন্য GitHub Pages-এর মতো ফ্রি Static Hosting ব্যবহার করা যায়। ওয়েবসাইটে শুধু অ্যাপের **কোড** থাকবে, তোমাদের ব্যক্তিগত টাকার হিসাব নয়। হিসাব ফোনেই থাকবে।

## ১. ফ্রি HTTPS-এ অ্যাপ প্রকাশ

1. GitHub-এ Login করে একটি **Public Repository** তৈরি করো, যেমন `tour-money`।
2. ZIP Extract করে `index.html`, `app.js`, `styles.css`, `sw.js`, `manifest.webmanifest`, এবং `icons/` ফোল্ডারটি Repository-এর **root**-এ Upload করো। **ব্যক্তিগত Backup JSON Upload করবে না।**
3. Repository-এর **Settings > Pages**-এ গিয়ে **Deploy from a branch**, `main`, `/ (root)` নির্বাচন করে Save করো।
4. Pages-এ যে HTTPS address দেখাবে, সেটি Safari-তে খোলো। অ্যাপের URL সাধারণত `https://USERNAME.github.io/REPOSITORY/`-এর মতো হয়; তোমার প্রকৃত URL GitHub Pages থেকেই নিতে হবে।

## ২. iPhone-এ Install

1. নিজের iPhone-এর **Safari** দিয়ে HTTPS URL খোলো (প্রথমবার Internet লাগবে)।
2. Safari-এর **Share > Add to Home Screen**-এ যাও। Option থাকলে **Open as Web App** On রাখো। তারপর **Add**।
3. Home Screen-এর **Tour Money** Icon দিয়ে একবার অ্যাপ খোলো, যাতে Offline Files Cache হতে পারে।
4. Airplane Mode চালু করে অ্যাপ আবার খোলো এবং পরীক্ষা করো। App offline না খুললে Internet চালু করে আবার খোলো, তারপর পুনরায় পরীক্ষা করো।

## ৩. ব্যবহারের নিয়ম

1. **Settings > Tour details** থেকে Tour Name ও Department Name দাও।
2. **Home > Add Fund > Initial fund**-এ ইতোমধ্যে জমা হওয়া মোট টাকা দাও।
3. **Add Expense** দিয়ে খরচ লিখো। Expense Date/Time স্বয়ংক্রিয়ভাবে আসবে; দরকারে Edit করা যায়।
4. **Reports** থেকে PDF/CSV Download ও Date-wise Expense Analysis দেখো।
5. **Settings > Export backup** দিয়ে নিয়মিত JSON File Apple Files/অন্য Device-এ Save করো।

## ৪. VP থেকে President-কে হিসাব দেখানো

1. VP: **Settings > Share viewer snapshot**।
2. Export হওয়া JSON File **AirDrop** করে President-এর iPhone-এ পাঠাও।
3. President: নিজের Tour Money App-এ **Settings > Import viewer snapshot** করে File বেছে নাও।
4. এখন President-এর অ্যাপ Read-only Mode-এ থাকবে; পরের Update দেখতে নতুন Snapshot পাঠাতে হবে। **এটি Live Sync নয়।**

## ৫. জরুরি সতর্কতা

- Safari / iOS Storage Delete হলে বা অ্যাপ Uninstall করলে একই Device-এর Local Data হারাতে পারে। **অন্য Device/Files-এ Manual Backup রাখা জরুরি।**
- Automatic Backup সর্বশেষ তিনটি রাখে, কিন্তু তিনটিই একই App Storage-এর ভিতরে থাকে।
- Real iPhone-এ পরীক্ষার আগে এটিকে চূড়ান্ত Accounting System হিসেবে ব্যবহার কোরো না।
- PDF-তে বাংলা নামের বদলে `?` আসতে পারে; সেক্ষেত্রে **Print / Save PDF** ব্যবহার করো।
- Android-এ Chrome দিয়ে একই HTTPS URL থেকে Install করা যায়।

## নতুন v1.2 আপডেট

- Expense যোগ করার সময় Category নিজে নির্বাচন করতে হবে, যাতে ভুল Category-তে Expense জমা না হয়।
- iPhone-এ Export করলে Browser support থাকলে Share Sheet আসবে; **Save to Files** বা **AirDrop** বেছে নাও।
- নিয়মিত **Settings > Export backup** ব্যবহার করো। ডিভাইসের ভেতরের তিনটি Automatic Backup আলাদা ফোনে Copy নয়।
- এই ZIP-এ তৈরি ফাইলগুলো আছে, কিন্তু এখনো Live URL/Hosting দেওয়া হয়নি। GitHub Pages-এ Publish করার পরেই Safari থেকে Add to Home Screen করা যাবে।
