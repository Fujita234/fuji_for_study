import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'firebaseDatabase.dart';

Future<void> main() async {
  await Firebase.initializeApp();  //firebaseの初期化を行います。awaitを使うためmainメソッドも非同期に対応させています。
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String newUserEmail = "";  //入力されたメアド
  String newUserPassword = "";  //入力されたパスワード
  String infoText = "";  //登録・ログインに関する情報を表示

  String loginUserEmail = ""; //入力されたメアド(ログイン)
  String loginUserPassword = ""; //入力されたパスワード(ログイン)

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("ユーザ登録＆ログイン機能です")),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(32),
          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: "メールアドレス"),
                onChanged: (String value) {
                  setState(() {
                    newUserEmail = value;
                  });
                },
              ),
              const SizedBox(height: 8),

              TextFormField(
                decoration: InputDecoration(labelText: "パスワード(6文字以上)"),
                obscureText: true,
                onChanged: (String value) {
                  setState(() {
                    newUserPassword = value;
                  });
                },
              ),
              const SizedBox(height: 8),

              ElevatedButton(
                onPressed: () async {
                  try {
                    //メールアドレス・パスワードでユーザー登録
                    final FirebaseAuth auth = FirebaseAuth.instance;
                    final UserCredential result = await auth.createUserWithEmailAndPassword(email: newUserEmail, password: newUserPassword);

                    //登録したユーザー情報
                    final User user = result.user;
                    setState(() {
                      infoText = "登録完了しました。:${user.email}";
                    });
                  } catch(e) {
                    // 登録失敗処理
                    setState(() {
                      infoText = "登録失敗しました。:${e.toString()}";
                    });
                  }
                },
                child: Text("ユーザー登録")
              ),
              const SizedBox(height: 8),

              TextFormField(
                decoration: InputDecoration(labelText: "メールアドレス"),
                onChanged: (String value) {
                  setState(() {
                    loginUserEmail = value;
                  });
                }
              ),

              TextFormField(
                decoration: InputDecoration(labelText: "パスワード"),
                onChanged: (String value) {
                  setState(() {
                    loginUserPassword = value;
                  });
                }
              ),
              const SizedBox(height: 8),

              ElevatedButton(
                onPressed: () async {
                  try {
                    //メアド・パスワード
                    final FirebaseAuth auth = FirebaseAuth.instance;
                    final UserCredential result = await auth.signInWithEmailAndPassword(email: loginUserEmail, password: loginUserPassword);

                    //ログイン成功処理
                    final User user = result.user;
                    setState(() {
                      infoText = "ログイン成功しました。${user.email}";
                    });
                  } catch(e) {
                    //ログイン失敗処理
                    setState(() {
                      infoText = "ログイン失敗しました。${e.toString()}";
                    });
                  }
                }, 
                child: Text("ログイン")
              ),
              const SizedBox(height: 8),

              Text(infoText), //状況をお伝えするテキスト

              ElevatedButton(
                child: Text("FirebaseCloudStoreの画面へ行く"),
                onPressed: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(builder: (context) => FirebaseDataBase())
                  );
                },
              )
            ],
          ),
        ),
      ),
    );
  }
}
