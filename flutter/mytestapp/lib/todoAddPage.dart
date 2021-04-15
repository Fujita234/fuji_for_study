import 'package:flutter/material.dart';

// タスク追加画面を作成
class TodoAddPage extends StatefulWidget {
  @override
  _TodoAddPageState createState() => _TodoAddPageState();
}

// State付きのWidgetはこう作る。
class _TodoAddPageState extends State<TodoAddPage> {
  // 最初にStateに入れる変数を宣言
  String _text = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("リスト追加"),
      ),
      body: Container(
        padding: EdgeInsets.all(64),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center, //こいつなに？
          children: [
            // 入力されたテキスト表示
            Text(_text, style: TextStyle(color: Colors.blue)),
            const SizedBox(height: 8),

            // テキストを打ち込む所
            TextField(
              onChanged: (String value) {
                setState(() {  //Stateに保存(set)している
                  _text = value;
                });
              },
            ),
            const SizedBox(height: 8),  //余白

            // リスト追加ボタン
            Container(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () {
                  showDialog(context: context, builder: (_) => FunkyOverlay());
                },
                child: Text("リスト追加", style: TextStyle(color: Colors.white)),
              ),
            ),
            const SizedBox(height: 8),  //余白

            // キャンセルボタン
            Container(
              width: double.infinity,
              child: TextButton(
                onPressed: () {
                  Navigator.of(context).pop(_text);
                },
                child: Text("キャンセル")
              )
            )
          ],
        )
      )
    );
  }
}


class FunkyOverlay extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => FunkyOverlayState();
}

class FunkyOverlayState extends State<FunkyOverlay> with SingleTickerProviderStateMixin {
  late AnimationController controller;
  late Animation<double> scaleAnimation;

  @override
  void initState() {
    super.initState();

    controller = AnimationController(vsync: this, duration: Duration(microseconds: 1));
    scaleAnimation = CurvedAnimation(parent: controller, curve: Curves.elasticInOut);

    controller.addListener(() {
      setState(() {});
    });

    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Material(
        color: Colors.transparent,
        child: ScaleTransition(
          scale: scaleAnimation,
          child: Container(
            decoration: ShapeDecoration(
              color: Colors.white,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(15.0)
              )
            ),
            child: Padding(
              padding: const EdgeInsets.all(50.0),
              child: Text("追加しました"),
            )
          ),
        )
      )
    );
  }
}