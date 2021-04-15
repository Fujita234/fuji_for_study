import 'package:flutter/material.dart';
import 'TodoListPage.dart';

void main() {
  runApp(MyTodoApp());
}

// テーマカラーなどを大まかなことを決めている。
class MyTodoApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My Todo App',
      theme: ThemeData(
        // テーマカラー
        primarySwatch: Colors.blue,
      ),
      // 中身
      home: TodoListPage(),
    );
  }
}