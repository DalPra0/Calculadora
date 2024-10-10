#include "mainwindow.h"
#include "ui_mainwindow.h"

double num1, num2;
QString operacao;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->button0, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button1, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button2, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button3, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button4, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button5, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button6, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button7, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button8, SIGNAL(released()), this, SLOT(digit_pressed()));
    connect(ui->button9, SIGNAL(released()), this, SLOT(digit_pressed()));

    connect(ui->buttonAdd, SIGNAL(released()), this, SLOT(operacao_pressed()));
    connect(ui->buttonSub, SIGNAL(released()), this, SLOT(operacao_pressed()));
    connect(ui->buttonMul, SIGNAL(released()), this, SLOT(operacao_pressed()));
    connect(ui->buttonDiv, SIGNAL(released()), this, SLOT(operacao_pressed()));

    connect(ui->buttonIgual, SIGNAL(released()), this, SLOT(equal_pressed()));
    connect(ui->buttonClear, SIGNAL(released()), this, SLOT(clear_pressed()));
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::digit_pressed() {
    QPushButton *button = (QPushButton*)sender();
    QString newLabel;
    newLabel = ui->label->text() + button->text();
    ui->label->setText(newLabel);
}

void MainWindow::operacao_pressed() {
    QPushButton *button = (QPushButton*)sender();
    num1 = ui->label->text().toDouble();
    operacao = button->text();
    ui->label->clear();
}

void MainWindow::equal_pressed() {
    num2 = ui->label->text().toDouble();
    double result;

    if (operacao == "+") {
        result = num1 + num2;
    } else if (operacao == "-") {
        result = num1 - num2;
    } else if (operacao == "*") {
        result = num1 * num2;
    } else if (operacao == "/") {
        if (num2 != 0)
            result = num1 / num2;
        else {
            ui->label->setText("Erro");
            return;
        }
    }

    ui->label->setText(QString::number(result));
}

void MainWindow::clear_pressed() {
    ui->label->clear();
}

