from tkinter import ttk
import sys, os, tkinter, json
from Storyboard import LoadStory, LoadTemplates, MakeSB, FilePath
from PIL import ImageShow


def ReloadStory():
    StoryDB = LoadStory("StoryDB")
    return StoryDB


class StoryBoardBuilder:
    def __init__(self):
        self.BuildGui()
        self.window.mainloop()

    def BuildGui(self):
        self.window = tkinter.Tk()
        self.window.title("StoryBoard Builder")
        self.window.geometry('900x650')
        self.SetScenarios()
        self.SetScenarioParts()

    def MakeAndShowImage(self):
        SBImage = MakeSB(self.Template.get(), self.BackGround.get(),
                         self.Face.get(),
                         self.Text.get("1.0", tkinter.END).strip("\n"),
                         self.Border.get(),
                         self.TextBorder.get(),
                         self.FaceBorder.get())
        ImageShow.show(SBImage)
        return

    def SetScenarios(self):
        self.CurrentScenario = ttk.Combobox(self.window, width=25)
        self.PostTextButton = tkinter.Button(self.window, text="Load Scenario ", command=self.SetScenarioParts)
        CurrentScenarioList = []
        StoryDB = ReloadStory()
        for each in StoryDB:
            CurrentScenarioList.append(each)
        self.CurrentScenario['values'] = CurrentScenarioList
        self.CurrentScenario.current(0)
        self.CurrentScenario.grid(column=0, row=0)
        self.PostTextButton.grid(column=1, row=0)

    def SaveScenarioPart(self):
        StoryDB = ReloadStory()

        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Template"] = self.Template.get()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["BackGround"] = self.BackGround.get()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Face"] = self.Face.get()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Text"] = self.Text.get("1.0",tkinter.END).strip("\n")
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Border"] = self.Border.get()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["TextBorder"] = self.TextBorder.get()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["FaceBorder"] = self.FaceBorder.get()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"] = self.ChoiceDict
        self.SaveStoryDB(StoryDB)

    def SetScenarioParts(self):
        self.ScenarioActs = ttk.Combobox(self.window, width=20)
        CurrentActsList = []
        StoryDB = ReloadStory()
        for each in StoryDB[self.CurrentScenario.get()]:
            CurrentActsList.append(each)
        self.ScenarioActs['values'] = CurrentActsList
        self.ScenarioActs.current(0)
        self.ScenarioActs.grid(column=0, row=3)
        self.PostTextButton = tkinter.Button(self.window, text="Load Part", command=self.SetDataEntry)
        self.PostTextButton.grid(column=1, row=3)

    def SetDataEntry(self):
        StoryDB = ReloadStory()

        if self.ScenarioActs.get() == "Info":
            self.Name = tkinter.Text(self.window, height=1, width=45)
            self.Name.insert("1.0", chars=StoryDB[self.CurrentScenario.get()]["Info"]["Name"])
            self.Name.grid(column=4, row=2)
            self.NameLabel = tkinter.Label(self.window, text="Name")
            self.NameLabel.grid(column=3, row=2)

            self.Description = tkinter.Text(self.window, height=4, width=45)
            self.Description.insert("1.0", chars=StoryDB[self.CurrentScenario.get()]["Info"]["Description"])
            self.Description.grid(column=4, row=3)
            self.DescriptionLabel = tkinter.Label(self.window, text="Description")
            self.DescriptionLabel.grid(column=3, row=3)


        else:
            self.Template = ttk.Combobox(self.window, height=1, width=45)
            AllTemplates = LoadTemplates()
            AllTemplatesList = []
            Count = -1
            Current = 0
            for each in AllTemplates:
                Count += 1
                AllTemplatesList.append(each)
                if each == StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Template"]:
                    Current = Count
            self.Template['values'] = AllTemplatesList
            self.Template.current(Current)
            self.Template.grid(column=4, row=5)
            self.TemplateLabel = tkinter.Label(self.window, text="Template")
            self.TemplateLabel.grid(column=3, row=5)

            self.BackGround = ttk.Combobox(self.window, height=1, width=45)
            AllImagesList = [""]
            if sys.platform == "linux" or sys.platform == "linux2":
                for file in os.listdir(f"{FilePath}/Files/Images/BackGround"):
                    AllImagesList.append(file.rstrip(".png"))
            if sys.platform == "win32" or sys.platform == "win64":
                for file in os.listdir(f"{FilePath}\\Files\\Images\\BackGround"):
                    AllImagesList.append(file.rstrip(".png"))
            Count = -1
            Current = 0
            for each in AllImagesList:
                Count += 1
                if each == StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["BackGround"]:
                    Current = Count
            self.BackGround['values'] = AllImagesList
            self.BackGround.current(Current)
            self.BackGround.grid(column=4, row=6)
            self.BackGroundLabel = tkinter.Label(self.window, text="BackGround")
            self.BackGroundLabel.grid(column=3, row=6)

            self.Face = ttk.Combobox(self.window, height=1, width=45)
            AllImagesList = [""]
            if sys.platform == "linux" or sys.platform == "linux2":
                for file in os.listdir(f"{FilePath}/Files/Images/Face"):
                    AllImagesList.append(file.rstrip(".png"))
            if sys.platform == "win32" or sys.platform == "win64":
                for file in os.listdir(f"{FilePath}\\Files\\Images\\Face"):
                    AllImagesList.append(file.rstrip(".png"))
            Count = -1
            Current = 0
            for each in AllImagesList:
                Count += 1
                if each == StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Face"]:
                    Current = Count
            self.Face['values'] = AllImagesList
            self.Face.current(Current)
            self.Face.grid(column=4, row=7)
            self.FaceLabel = tkinter.Label(self.window, text="Face")
            self.FaceLabel.grid(column=3, row=7)


            if StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Text"] is None or "":
                self.Text = tkinter.Text(self.window, height=8, width=45)
                self.Text.insert("1.0", chars="")
                self.Text.grid(column=4, row=8)
                self.TextLabel = tkinter.Label(self.window, text="Text")
                self.TextLabel.grid(column=3, row=8)

            else:
                self.Text = tkinter.Text(self.window, height=8, width=45)
                self.Text.insert("1.0", chars=StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Text"])
                self.Text.grid(column=4, row=8)
                self.TextLabel = tkinter.Label(self.window, text="Text")
                self.TextLabel.grid(column=3, row=8)


            self.Border = ttk.Combobox(self.window, height=1, width=45)
            AllImagesList = [""]
            if sys.platform == "linux" or sys.platform == "linux2":
                for file in os.listdir(f"{FilePath}/Files/Images/Border"):
                    AllImagesList.append(file.rstrip(".png"))
            if sys.platform == "win32" or sys.platform == "win64":
                for file in os.listdir(f"{FilePath}\\Files\\Images\\Border"):
                    AllImagesList.append(file.rstrip(".png"))
            Count = -1
            Current = 0
            for each in AllImagesList:
                Count += 1
                if each == StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Border"]:
                    Current = Count
            self.Border['values'] = AllImagesList
            self.Border.current(Current)
            self.Border.grid(column=4, row=9)
            self.BorderLabel = tkinter.Label(self.window, text="Border")
            self.BorderLabel.grid(column=3, row=9)

            self.TextBorder = ttk.Combobox(self.window, height=1, width=45)
            AllImagesList = [""]
            if sys.platform == "linux" or sys.platform == "linux2":
                for file in os.listdir(f"{FilePath}/Files/Images/TextBorder"):
                    AllImagesList.append(file.rstrip(".png"))
            if sys.platform == "win32" or sys.platform == "win64":
                for file in os.listdir(f"{FilePath}\\Files\\Images\\TextBorder"):
                    AllImagesList.append(file.rstrip(".png"))
            Count = -1
            Current = 0
            for each in AllImagesList:
                Count += 1
                if each == StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["TextBorder"]:
                    Current = Count
            self.TextBorder['values'] = AllImagesList
            self.TextBorder.current(Current)
            self.TextBorder.grid(column=4, row=10)
            self.TextBorderLabel = tkinter.Label(self.window, text="Text Border")
            self.TextBorderLabel.grid(column=3, row=10)

            self.FaceBorder = ttk.Combobox(self.window, height=1, width=45)
            AllImagesList = [""]
            if sys.platform == "linux" or sys.platform == "linux2":
                for file in os.listdir(f"{FilePath}/Files/Images/FaceBorder"):
                    AllImagesList.append(file.rstrip(".png"))
            if sys.platform == "win32" or sys.platform == "win64":
                for file in os.listdir(f"{FilePath}\\Files\\Images\\FaceBorder"):
                    AllImagesList.append(file.rstrip(".png"))
            Count = -1
            Current = 0
            for each in AllImagesList:
                Count += 1
                if each == StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["FaceBorder"]:
                    Current = Count
            self.FaceBorder['values'] = AllImagesList
            self.FaceBorder.current(Current)
            self.FaceBorder.grid(column=4, row=11)
            self.FaceBorderLabel = tkinter.Label(self.window, text="Face Border")
            self.FaceBorderLabel.grid(column=3, row=11)

            self.ChoiceDict = {}
            self.CurrentChoices = ttk.Combobox(self.window, width=20)
            CurrentChoicesList = []
            StoryDB = ReloadStory()
            for each in StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"]:
                CurrentChoicesList.append(each)
            self.CurrentChoices['values'] = CurrentChoicesList
            self.CurrentChoices.current(0)
            self.UpdateChoiceDict()
            self.LoadCurrentChoices = ttk.Button(self.window, width=20, text="Load Choice",
                                                 command=self.UpdateChoiceDisply)
            self.CurrentChoices.grid(column=1, row=12)
            self.LoadCurrentChoices.grid(column=1, row=13)
            self.UpdateChoiceDisply()

        ShowImageButton = tkinter.Button(text="Show Image", command=self.MakeAndShowImage)
        ShowImageButton.grid(column=0, row=6)

        SavePartButton = tkinter.Button(text="Save Part", command=self.SaveScenarioPart)
        SavePartButton.grid(column=1, row=7)

        AddPartButton = tkinter.Button(text="New Part", command=self.AddScenarioPart)
        AddPartButton.grid(column=1, row=8)

        AddChoiceButton = tkinter.Button(text="Add Choice", command=self.AddChoice)
        AddChoiceButton.grid(column=1, row=5)

        DeleteChoiceButton = tkinter.Button(text="Delete Choice", command=self.DeleteChoice)
        DeleteChoiceButton.grid(column=1, row=6)

        NewScenarioButton = tkinter.Button(text="New Scenario", command=self.MakeNewScenario)
        NewScenarioButton.grid(column=0, row=7)

        DeleteScenarioButton = tkinter.Button(text="Delete Scenario", command=self.DeleteScenario)
        DeleteScenarioButton.grid(column=0, row=8)

    def DeleteScenario(self):
        StoryDB = ReloadStory()
        StoryDB.pop(self.CurrentScenario.get())
        self.SaveStoryDB(StoryDB)
        self.SetScenarios()

    def MakeNewScenario(self):
        self.top = tkinter.Toplevel(name="scenario part adder")
        self.top.geometry("500x150")
        self.NewScenarioName = tkinter.Text(self.top, width=25, height=1)
        self.NewScenarioName.grid(column=1, row=1)
        self.NewScenarioNameLabel = tkinter.Label(self.top, text="Name")
        self.NewScenarioNameLabel.grid(column=0, row=1)

        self.NewScenarioDescription = tkinter.Text(self.top, width=50, height=4)
        self.NewScenarioDescription.grid(column=1, row=2)
        self.NewScenarioNameDescription = tkinter.Label(self.top, text="Description")
        self.NewScenarioNameDescription.grid(column=0, row=2)

        # Create a Button to print something in the Entry widget
        AddButton = tkinter.Button(self.top, text="Add Scenario", command=self.MakeScenario)
        AddButton.grid(column=1, row=3)

    def MakeScenario(self):

        StoryDB = ReloadStory()
        StoryDB[self.NewScenarioName.get("1.0", tkinter.END).strip("\n")] = {"Info":
                                                                                 {"Name": self.NewScenarioName.get(
                                                                                     "1.0", tkinter.END).strip("\n"),
                                                                                  "Description": self.NewScenarioDescription.get(
                                                                                      "1.0", tkinter.END).rstrip("\n")}}
        self.top.destroy()
        self.SaveStoryDB(StoryDB)
        self.SetScenarios()

    def UpdateChoiceDict(self):
        StoryDB = ReloadStory()
        for each in StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"]:
            self.ChoiceDict[each] = \
                {"Reward": StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][each]["Reward"],
                 "Requirement": StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][each][
                     "Requirement"],
                 "Price": StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][each]["Price"],
                 "Destination": StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][each][
                     "Destination"],
                 "Color": StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][each]["Color"],
                 "Command": StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][each]["Command"]}

    def UpdateChoiceDisply(self):
        self.ChoiceRow = 11

        ChoiceName = tkinter.Text(self.window, height=1, width=45)
        ChoiceName.insert("1.0", chars=self.CurrentChoices.get())
        self.ChoiceRow += 1
        ChoiceName.grid(column=4, row=self.ChoiceRow)
        ChoiceNameLabel = tkinter.Label(self.window, text="Choice Name")
        ChoiceNameLabel.grid(column=3, row=self.ChoiceRow)

        ChoiceReward = tkinter.Text(self.window, height=1, width=45)
        if self.ChoiceDict[self.CurrentChoices.get()]["Reward"] is None or "":
            ChoiceReward.insert("1.0", chars="")
        else:
            ChoiceReward.insert("1.0", chars=self.ChoiceDict[self.CurrentChoices.get()]["Reward"])
        self.ChoiceRow += 1
        ChoiceReward.grid(column=4, row=self.ChoiceRow)
        ChoiceRewardLabel = tkinter.Label(self.window, text=f"Reward")
        ChoiceRewardLabel.grid(column=3, row=self.ChoiceRow)

        ChoiceRequirement = tkinter.Text(self.window, height=1, width=45)
        if self.ChoiceDict[self.CurrentChoices.get()]["Reward"] is None or "":
            ChoiceRequirement.insert("1.0", chars="")
        else:
            ChoiceRequirement.insert("1.0", chars=self.ChoiceDict[self.CurrentChoices.get()]["Requirement"])

        self.ChoiceRow += 1
        ChoiceRequirement.grid(column=4, row=self.ChoiceRow)
        ChoiceRequirementLabel = tkinter.Label(self.window, text=f"Requirement")
        ChoiceRequirementLabel.grid(column=3, row=self.ChoiceRow)

        ChoicePrice = tkinter.Text(self.window, height=1, width=45)
        if self.ChoiceDict[self.CurrentChoices.get()]["Reward"] is None or "":
            ChoicePrice.insert("1.0", chars="")
        else:
            ChoicePrice.insert("1.0", chars=self.ChoiceDict[self.CurrentChoices.get()]["Price"])

        self.ChoiceRow += 1
        ChoicePrice.grid(column=4, row=self.ChoiceRow)
        ChoicePriceLabel = tkinter.Label(self.window, text=f"Price")
        ChoicePriceLabel.grid(column=3, row=self.ChoiceRow)

        ChoiceDestination = tkinter.Text(self.window, height=1, width=45)
        if self.ChoiceDict[self.CurrentChoices.get()]["Destination"] is None or "":
            ChoiceDestination.insert("1.0", chars="")
        else:
            ChoiceDestination.insert("1.0", chars=self.ChoiceDict[self.CurrentChoices.get()]["Destination"])

        self.ChoiceRow += 1
        ChoiceDestination.grid(column=4, row=self.ChoiceRow)
        ChoiceDestinationLabel = tkinter.Label(self.window, text=f"Destination")
        ChoiceDestinationLabel.grid(column=3, row=self.ChoiceRow)

        ChoiceColor = tkinter.Text(self.window, height=1, width=45)
        if self.ChoiceDict[self.CurrentChoices.get()]["Color"] is None or "":
            ChoiceColor.insert("1.0", chars="")
        else:
            ChoiceColor.insert("1.0", chars=self.ChoiceDict[self.CurrentChoices.get()]["Color"])
        self.ChoiceRow += 1
        ChoiceColor.grid(column=4, row=self.ChoiceRow)
        ChoiceColorLabel = tkinter.Label(self.window, text=f"Color")
        ChoiceColorLabel.grid(column=3, row=self.ChoiceRow)

        ChoiceCommand = tkinter.Text(self.window, height=1, width=45)
        if self.ChoiceDict[self.CurrentChoices.get()]["Command"] is None or "":
            ChoiceCommand.insert("1.0", chars="")
        else:
            ChoiceCommand.insert("1.0", chars=self.ChoiceDict[self.CurrentChoices.get()]["Command"])

        self.ChoiceRow += 1
        ChoiceCommand.grid(column=4, row=self.ChoiceRow)
        ChoiceCommandLabel = tkinter.Label(self.window, text=f"Command")
        ChoiceCommandLabel.grid(column=3, row=self.ChoiceRow)


    def DeleteChoice(self):
        StoryDB = ReloadStory()
        del StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"][self.CurrentChoices.get()]
        self.SaveStoryDB(StoryDB)
        self.UpdateChoiceDict()
        self.UpdateChoiceDisply()

    def AddChoice(self):
        self.top = tkinter.Toplevel(name="update choice")
        self.top.geometry("230x175")
        self.NewName = tkinter.Entry(self.top, width=25)
        self.NewName.grid(column=1, row=0)
        self.NewNameLabel = tkinter.Label(self.top, text="Name", width=9)
        self.NewNameLabel.grid(column=0, row=0)
        self.NewReward = tkinter.Entry(self.top, width=25)
        self.NewReward.grid(column=1, row=1)
        self.NewRewardLabel = tkinter.Label(self.top, text="Reward", width=9)
        self.NewRewardLabel.grid(column=0, row=1)
        self.NewRequirement = tkinter.Entry(self.top, width=25)
        self.NewRequirement.grid(column=1, row=2)
        self.NewRequirementLabel = tkinter.Label(self.top, text="Requirement", width=9)
        self.NewRequirementLabel.grid(column=0, row=2)
        self.NewPrice = tkinter.Entry(self.top, width=25)
        self.NewPrice.grid(column=1, row=3)
        self.NewPriceLabel = tkinter.Label(self.top, text="Price", width=9)
        self.NewPriceLabel.grid(column=0, row=3)
        self.NewDestination = tkinter.Entry(self.top, width=25)
        self.NewDestination.grid(column=1, row=4)
        self.NewDestinationLabel = tkinter.Label(self.top, text="Destination", width=9)
        self.NewDestinationLabel.grid(column=0, row=4)

        self.NewColor = ttk.Combobox(self.top, height=1)
        colors = ["green", "red", "grey", "blurple"]
        self.NewColor['values'] = colors
        self.NewColor.current(0)

        self.NewColor.grid(column=1, row=5)
        self.NewColorLabel = tkinter.Label(self.top, text="Color", width=9)
        self.NewColorLabel.grid(column=0, row=5)


        self.NewCommand = tkinter.Entry(self.top, width=25)
        self.NewCommand.grid(column=1, row=6)
        self.NewCommandLabel = tkinter.Label(self.top, text="Command", width=9)
        self.NewCommandLabel.grid(column=0, row=6)



        AddButton = tkinter.Button(self.top, text="Add", command=self.AddChoiceToDict)
        AddButton.grid(column=1, row=7)

    def AddChoiceToDict(self):
        self.ChoiceDict[self.NewName.get()] = \
            {"Reward": self.NewReward.get(),
             "Requirement": self.NewRequirement.get(),
             "Price": self.NewPrice.get(),
             "Destination": self.NewDestination.get(),
             "Color": self.NewColor.get(),
             "Command": self.NewCommand.get()}
        StoryDB = ReloadStory()
        StoryDB[self.CurrentScenario.get()][self.ScenarioActs.get()]["Choices"] = self.ChoiceDict
        self.SaveStoryDB(StoryDB)
        self.UpdateChoiceDisply()
        self.top.destroy()

    def SaveStoryDB(self, StoryDB):
        if sys.platform == "linux" or sys.platform == "linux2":
            with open(f"{FilePath}/Files/Storys/StoryDB.json", "w") as JSON:
                json.dump(StoryDB, JSON)
        if sys.platform == "win32" or sys.platform == "win64":
            with open(f"{FilePath}\\Files\\Storys\\StoryDB.json", "w") as JSON:
                json.dump(StoryDB, JSON)

    def AddScenarioPart(self):
        self.top = tkinter.Toplevel(name="scenario part adder")
        self.top.geometry("100x100")
        self.NewPartName = tkinter.Entry(self.top, width=25)
        self.NewPartName.pack()

        # Create a Button to print something in the Entry widget
        AddButton = tkinter.Button(self.top, text="Add", command=self.AddPart)
        AddButton.pack(pady=5, side=tkinter.TOP)

    def AddPart(self):
        StoryDB = ReloadStory()
        StoryDB[self.CurrentScenario.get()][self.NewPartName.get()] = {"Template": "800x200R", "BackGround": None,
                                                                       "Face": None,
                                                                       "Text": None, "Border": None, "TextBorder": None,
                                                                       "FaceBorder": None, "TextBorder": None,
                                                                       "Choices": {
                                                                           "Next": {"Reward": None, "Requirement": None,
                                                                                    "Price": None, "Destination": "10",
                                                                                    "Color": "green", "Command": None}}}

        if sys.platform == "linux" or sys.platform == "linux2":
            with open(f"{FilePath}/Files/Storys/StoryDB.json", "w") as JSON:
                json.dump(StoryDB, JSON)
        if sys.platform == "win32" or sys.platform == "win64":
            with open(f"{FilePath}\\Files\\Storys\\StoryDB.json", "w") as JSON:
                json.dump(StoryDB, JSON)
        self.SetScenarios()
        self.SetScenarioParts()
        self.top.destroy()


StoryBoardBuilder()
