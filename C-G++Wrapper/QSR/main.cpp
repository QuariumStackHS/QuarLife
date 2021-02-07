#include "includes/config.hpp"
#include "../Cfg.hpp"
/*
Args parser, analyze and execute
*/
class Argser
{
public:
    Argser(int, char **);
    int Parse();
    int Update();
private:

    int Compile();
    int Link();
    int Run();

    Configurator Cfg = Configurator();
    int argc;
    char **argv;
};
int Argser::Run(){
    string Cmd01 = "./Build/exe/";
    string Cmd02 = Cfg.ProgrameName;
    string Cmd03 = ".exe";
    string Cmd = Cmd01.append(Cmd02);
    string Cmd1 = Cmd.append(Cmd03);

    cout << "Running using: \"" << Cmd << "\" | Return: " << system(Cmd1.c_str()) << endl;
    return 0;
}
int Argser::Link()
{
    string Cmd01 = "g++ Build/obj/*.QSRobj -o Build/exe/";
    string Cmd02 = Cfg.ProgrameName;
    string Cmd03 = ".exe -std=c++";
    string Cmd = Cmd01.append(Cmd02);
    string Cmd1 = Cmd.append(Cmd03);
    string Cmd04=to_string(Cfg.CPPLang);
    string Cmd2 = Cmd1.append(Cmd04);

    cout << "Linking using: \"" << Cmd2 << "\" | Return: " << system(Cmd2.c_str()) << endl;
    return 0;
}
int Argser::Update()
{ int i=system("g++ QSR/main.cpp -std=c++17 -o QSR.E");
if (strcmp(this->argv[1],"update")==0){
    cout<<"\nRecompiling QSR:"<<endl;
    cout << "\tUpdating configuration.." << endl;
    cout << "\tCompiling QSR With Return code: " << i<< endl;}
    exit(0);
    return 0;
}
int Argser::Compile()
{
    if(this->argc==2){
        cout<<"Compile need at least 2 args exemple: ./QSR compile main"<<endl;
    }
    else{
    string Cmd01 = "g++ src/";
    string Cmd02 = this->argv[2];
    string Cmd03 = "/main.cpp -c -o Build/obj/";
    string Cmd = Cmd01.append(Cmd02);
    string Cmd1 = Cmd.append(Cmd03);
    string Cmd2 = Cmd1.append(Cmd02);
    string Cmd3 = Cmd2.append(".QSRobj -Iincludes -std=c++");
    string Cmd04=to_string(Cfg.CPPLang);
    string Cmd05 = Cmd3.append(Cmd04);
    cout << "Compile using: \"" << Cmd05 << "\" | Return: " << system(Cmd3.c_str()) << endl;}

    return 0;
}
int Argser::Parse()
{

    if (strcmp(this->argv[1], "init") == 0)
    {
        system("mkdir QSR");
        system("mksir QSR/Private");
        system("mkdir Src");
        system("mkdir includes");
        system("mkdir Build");
        system("mkdir Build/obj");
        system("mkdir Build/exe");
    }
    else if (strcmp(this->argv[1],"Link")==0){
        Link();
        
    }
    else if (strcmp(this->argv[1],"build")==0){
        Compile();
        Link();
    }
    else if (strcmp(this->argv[1],"run")==0){
        Run();
    }
    else if (strcmp(this->argv[1], "add") == 0)
    {

        string Cmd00 = "mkdir src/";
        string Cmd01 = this->argv[2];
        string Cmd02 = Cmd00.append(Cmd01);
        system(Cmd02.c_str());
        string Cmd03 = "mkdir includes/";
        string Cmd04 = this->argv[2];
        string Cmd05 = Cmd03.append(Cmd04);
        system(Cmd05.c_str());
        /*
        
        
        */
    }
    else if (strcmp(this->argv[1], "update") == 0)
    {
        Update();
        //system("g++ -c Cfg.hpp -o QSR/Private/Config.obj");
        //system("g++ QSR/Private/*.obj -o QSR.E");
    }
    else if (strcmp(this->argv[1],"test")==0){
                Compile();
        Link();
        Run();
    }
    else if (strcmp(this->argv[1], "compile") == 0)
    {
        Compile();
        //system()
    }
    return 0;
}
Argser::Argser(int argc, char **argv)
{
    this->argc = argc;
    this->argv = argv;
}

int main(int argc, char **argv)
{
    cout << "-------QSR compiler-------" << endl;

    try
    {
        Argser Args = Argser(argc, argv);
        
        Args.Parse();
        Args.Update();
    }
    catch (const std::exception &e)
    {
        cout <<"Error: "<< e.what() << endl;
    }
    return 0;
}