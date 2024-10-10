using System;
using System.Windows.Forms;

namespace Calculadora {
    public partial class Form1 : Form {
        double num1, num2;
        string operacao;

        public Form1() {
            InitializeComponent();
        }

        private void button_Click(object sender, EventArgs e) {
            Button button = (Button)sender;
            if (textBox1.Text == "0")
                textBox1.Text = "";
            textBox1.Text += button.Text;
        }

        private void operacao_Click(object sender, EventArgs e) {
            Button button = (Button)sender;
            num1 = double.Parse(textBox1.Text);
            operacao = button.Text;
            textBox1.Text = "";
        }

        private void buttonIgual_Click(object sender, EventArgs e) {
            num2 = double.Parse(textBox1.Text);
            switch (operacao) {
                case "+":
                    textBox1.Text = (num1 + num2).ToString();
                    break;
                case "-":
                    textBox1.Text = (num1 - num2).ToString();
                    break;
                case "*":
                    textBox1.Text = (num1 * num2).ToString();
                    break;
                case "/":
                    if (num2 != 0)
                        textBox1.Text = (num1 / num2).ToString();
                    else
                        textBox1.Text = "Erro";
                    break;
            }
        }

        private void buttonClear_Click(object sender, EventArgs e) {
            textBox1.Text = "0";
        }
    }
}

