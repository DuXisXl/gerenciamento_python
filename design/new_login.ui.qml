/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.5
import QtQuick.Controls 6.5
import UntitledProject

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello UntitledProject")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }



    Image {
        id: desktop1
        x: -748
        y: -104
        width: 3396
        height: 1396
        source: "../../../Downloads/new_login/Desktop - 1.png"
        fillMode: Image.PreserveAspectFit

        TextInput {
            id: txt_login
            x: 1480
            y: 668
            width: 440
            height: 64
            text: qsTr("Text Input")
            font.pixelSize: 12
        }

        TextInput {
            id: txt_password
            x: 1480
            y: 756
            width: 440
            height: 64
            text: qsTr("Text Input")
            font.pixelSize: 12
        }

        Button {
            id: btn_login
            x: 1604
            y: 886
            width: 190
            height: 64
            visible: false
            text: qsTr("Button")
        }
    }
    Image {
        id: key
        x: 738
        y: 658
        width: 44
        height: 62
        source: "../../../Downloads/new_login/key.png"
        fillMode: Image.PreserveAspectFit
    }
    Image {
        id: account
        x: 736
        y: 573
        width: 46
        height: 43
        source: "../../../Downloads/new_login/account.png"
        fillMode: Image.PreserveAspectFit
    }
}
