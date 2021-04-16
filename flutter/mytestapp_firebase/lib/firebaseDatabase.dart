import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class FirebaseDataBase extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Flutter Firebase Demo",
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyFirestorePage(),
    );
  }
}


class MyFirestorePage extends StatefulWidget {
  @override
  _MyFirestorePageState createState() => _MyFirestorePageState();
}

class _MyFirestorePageState extends State<MyFirestorePage> {
  List<DocumentSnapshot> documentList = [];
  String orderDocumentInfo = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          children: [
            ElevatedButton(
              child: Text("コレクション＋ドキュメント作成"),
              onPressed: () async {
                //ドキュメント作成
                await FirebaseFirestore.instance
                  .collection("users")
                  .doc('id_user')
                  .set({"name": "鈴木", "age": 40});  //データセット
              },
            ),
            ElevatedButton(
              child: Text("サブコレクション＋ドキュメント作成"),
              onPressed: () async {
                await FirebaseFirestore.instance
                  .collection("users")
                  .doc('id_user')
                  .collection('orders')
                  .doc("id_order")
                  .set({"price": 600, "date": "9/13"});
              }
            ),

            ElevatedButton(
              child: Text("ドキュメント一覧取得"), 
              onPressed: () async {
                final snapshot = await FirebaseFirestore.instance.collection("users").get();
                setState(() {
                  documentList = snapshot.docs;
                });
              }
            ),

            Column(
              children: documentList.map((document) {
                return ListTile(
                  title: Text("${document['name']}さん"),
                  subtitle: Text("${document['age']}歳"),
                );
              }).toList(),
            ),

            ElevatedButton(
              child: Text("ドキュメントを指定して取得"),
              onPressed: () async {
                final document = await FirebaseFirestore.instance
                  .collection("users")
                  .doc("id_user")
                  .collection("orders")
                  .doc("id_order")
                  .get();

                setState(() {
                  orderDocumentInfo = "${document['date']} ${document['price']}円";
                });
              },
            ),

            ListTile(title: Text(orderDocumentInfo)),
          ]
        ),)
    );
  }
}