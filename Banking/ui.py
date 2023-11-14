<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>4095</width>
    <height>960</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>550</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="widget" native="true">
    <property name="geometry">
     <rect>
      <x>-170</x>
      <y>440</y>
      <width>120</width>
      <height>80</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="Login_widget" native="true">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>10</y>
      <width>521</width>
      <height>661</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>641</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>90</y>
       <width>151</width>
       <height>71</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>25</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,210);
</string>
     </property>
     <property name="text">
      <string>Log In</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit">
     <property name="geometry">
      <rect>
       <x>120</x>
       <y>210</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Account Number</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_2">
     <property name="geometry">
      <rect>
       <x>120</x>
       <y>300</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Password</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Login">
     <property name="geometry">
      <rect>
       <x>110</x>
       <y>410</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>15</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#Login {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
transition: 0.9s;
}

QPushButton#Login:hover {
background-color:qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#Login:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Log In</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>210</x>
       <y>480</y>
       <width>121</width>
       <height>50</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,200);
</string>
     </property>
     <property name="text">
      <string>Don't have acount?</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Create_account">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>530</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#Create_account {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#Create_account:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#Create_account:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Create Account</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="Create_account_widget" native="true">
    <property name="geometry">
     <rect>
      <x>620</x>
      <y>10</y>
      <width>521</width>
      <height>661</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>641</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="label_5">
     <property name="geometry">
      <rect>
       <x>140</x>
       <y>70</y>
       <width>261</width>
       <height>71</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>20</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,210);
</string>
     </property>
     <property name="text">
      <string>Create Account</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_3">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>170</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Name</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_4">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>330</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Create Password</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Create_account_2">
     <property name="geometry">
      <rect>
       <x>200</x>
       <y>510</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#Create_account_2 {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#Create_account_2:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#Create_account_2:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Create Account</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_5">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>410</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Deposit Amount</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_6">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>250</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Phone Number</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="Banking" native="true">
    <property name="geometry">
     <rect>
      <x>1170</x>
      <y>10</y>
      <width>1061</width>
      <height>661</height>
     </rect>
    </property>
    <widget class="QLabel" name="label_6">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>10</y>
       <width>1021</width>
       <height>641</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-image:url(:/images/rupee.jpg);
border-radius:10px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="deposit">
     <property name="geometry">
      <rect>
       <x>640</x>
       <y>180</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>15</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#deposit {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
transition: 0.9s;
}

QPushButton#deposit:hover {
background-color:qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#deposit:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Deposit</string>
     </property>
    </widget>
    <widget class="QPushButton" name="withdrawl">
     <property name="geometry">
      <rect>
       <x>640</x>
       <y>270</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>15</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#withdrawl {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
transition: 0.9s;
}

QPushButton#withdrawl:hover {
background-color:qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#withdrawl:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Withdrawl</string>
     </property>
    </widget>
    <widget class="QPushButton" name="transfer">
     <property name="geometry">
      <rect>
       <x>640</x>
       <y>360</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>15</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#transfer {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
transition: 0.9s;
}

QPushButton#transfer:hover {
background-color:qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#transfer:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Transfer</string>
     </property>
    </widget>
    <widget class="QPushButton" name="check_balance">
     <property name="geometry">
      <rect>
       <x>640</x>
       <y>450</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>15</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#check_balance {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
transition: 0.9s;
}

QPushButton#check_balance:hover {
background-color:qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#check_balance:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Check Balance</string>
     </property>
    </widget>
    <widget class="QPushButton" name="log_out">
     <property name="geometry">
      <rect>
       <x>910</x>
       <y>580</y>
       <width>101</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#log_out {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
transition: 0.9s;
}

QPushButton#log_out:hover {
background-color:qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#log_out:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Log Out</string>
     </property>
    </widget>
    <widget class="QLabel" name="user_icon">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>40</y>
       <width>31</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-image:url(:/images/icons8-user-24.png) 0 0 0 0 stretch stretch;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="user_name">
     <property name="geometry">
      <rect>
       <x>90</x>
       <y>50</y>
       <width>351</width>
       <height>16</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,200);</string>
     </property>
     <property name="text">
      <string>User Name</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_7">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>50</y>
       <width>131</width>
       <height>20</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,200);
</string>
     </property>
     <property name="text">
      <string>Account Number:</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_8">
     <property name="geometry">
      <rect>
       <x>820</x>
       <y>50</y>
       <width>131</width>
       <height>20</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,200);
</string>
     </property>
     <property name="text">
      <string>XXX XXX XXX</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="diposit_widget" native="true">
    <property name="geometry">
     <rect>
      <x>2390</x>
      <y>10</y>
      <width>521</width>
      <height>451</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label_9">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>411</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="deposit_head">
     <property name="geometry">
      <rect>
       <x>200</x>
       <y>70</y>
       <width>151</width>
       <height>71</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>20</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,210);
</string>
     </property>
     <property name="text">
      <string>Dioposit</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="deposit_amount">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>190</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Enter Amount</string>
     </property>
    </widget>
    <widget class="QPushButton" name="deposit_ok">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>310</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#deposit_ok {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#deposit_ok:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#deposit_ok:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Ok</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="withdrawl_widget" native="true">
    <property name="geometry">
     <rect>
      <x>2980</x>
      <y>10</y>
      <width>521</width>
      <height>451</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label_15">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>411</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="withdrawl_head">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>70</y>
       <width>181</width>
       <height>71</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>20</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,210);
</string>
     </property>
     <property name="text">
      <string>Withdraw</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="withdrawl_amount">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>190</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Enter Amount</string>
     </property>
    </widget>
    <widget class="QPushButton" name="withdrawl_ok">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>310</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#withdrawl_ok {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#withdrawl_ok:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#withdrawl_ok:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Ok</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="transfer_widget" native="true">
    <property name="geometry">
     <rect>
      <x>3550</x>
      <y>10</y>
      <width>521</width>
      <height>451</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label16">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>411</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="transfer_head">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>70</y>
       <width>181</width>
       <height>71</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>20</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,210);
</string>
     </property>
     <property name="text">
      <string>Transfer</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="transfer_account">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>160</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Receiver Account NUmber</string>
     </property>
    </widget>
    <widget class="QPushButton" name="transfer_ok">
     <property name="geometry">
      <rect>
       <x>200</x>
       <y>340</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#transfer_ok {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#transfer_ok:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#transfer_ok:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Ok</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="transfer_amount">
     <property name="geometry">
      <rect>
       <x>130</x>
       <y>240</y>
       <width>300</width>
       <height>50</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color:rgba(0,0,0,0);
border:none;
border-bottom:2px solid rgb(240, 240, 250);
color:rgba(255,255,255,190);
padding:7px;
</string>
     </property>
     <property name="placeholderText">
      <string>Enter Amount</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="balance_widget" native="true">
    <property name="geometry">
     <rect>
      <x>2980</x>
      <y>480</y>
      <width>521</width>
      <height>371</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label16_3">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>341</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="balance_ok">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>280</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#balance_ok {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#balance_ok:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#balance_ok:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Ok</string>
     </property>
    </widget>
    <widget class="QLabel" name="available_balance_head">
     <property name="geometry">
      <rect>
       <x>120</x>
       <y>100</y>
       <width>301</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>20</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,200);
</string>
     </property>
     <property name="text">
      <string>Available Balance</string>
     </property>
    </widget>
    <widget class="QLabel" name="balance_amount">
     <property name="geometry">
      <rect>
       <x>230</x>
       <y>170</y>
       <width>151</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>18</pointsize>
       <underline>true</underline>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,230);
</string>
     </property>
     <property name="text">
      <string>XXXX</string>
     </property>
    </widget>
    <widget class="QLabel" name="rupee_icon">
     <property name="geometry">
      <rect>
       <x>200</x>
       <y>178</y>
       <width>31</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-image:  url(:/images/icons8-rupee-96.png) 0 0 0 0 stretch stretch;
opacity:0.3;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="transaction_completed_widget" native="true">
    <property name="geometry">
     <rect>
      <x>3560</x>
      <y>500</y>
      <width>521</width>
      <height>261</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton #pushButton{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 68, 235), stop:1 rgba(255, 255, 255, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton #pushButton:hover{
background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0.778455, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(255, 255, 255, 255))
color:red;
}</string>
    </property>
    <widget class="QLabel" name="label16_4">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>461</width>
       <height>241</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image:url(:/images/rupee1.jpg);
background-repeat: no-repeat;
background-size: (831,441);
border-radius: 20px;
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="transaction_completed_ok">
     <property name="geometry">
      <rect>
       <x>190</x>
       <y>190</y>
       <width>150</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton#transaction_completed_ok {
background-color:qlineargradient(spread:pad, x1:0, y1:0.897, x2:1, y2:0.631, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
color:rgba(255,255,255,200);
border-radius:10px;
}

QPushButton#transaction_completed_ok:hover {
background-color: qlineargradient(spread:pad, x1:0.134328, y1:0.846, x2:0.925, y2:0.142, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(10, 63, 131, 255));
}

QPushButton#transaction_completed_ok:pressed {
   padding-left:5px;
   padding-right:5px;
   padding-top:5px;
}</string>
     </property>
     <property name="text">
      <string>Ok</string>
     </property>
    </widget>
    <widget class="QLabel" name="transation_completed_head">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>50</y>
       <width>391</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>20</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color:rgba(255,255,255,200);
</string>
     </property>
     <property name="text">
      <string>Transaction Succesful</string>
     </property>
    </widget>
    <widget class="QLabel" name="completed_icon">
     <property name="geometry">
      <rect>
       <x>230</x>
       <y>110</y>
       <width>61</width>
       <height>61</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-image:url(:/images/checklist.png) 0 0 0 0 stretch stretch;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>4095</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="images/resources.qrc"/>
 </resources>
 <connections/>
</ui>
