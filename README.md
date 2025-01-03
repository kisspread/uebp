# MkDocs BlueprintUE Plugin

A MkDocs plugin that renders Unreal Engine Blueprint nodes in your documentation. Based on the excellent [blueprintue-self-hosted-edition](https://github.com/blueprintue/blueprintue-self-hosted-edition) project.

## Features

- Render Unreal Engine Blueprint nodes in your MkDocs documentation
- Support both local blueprint text and blueprintue.com links
- Interactive node visualization with pan and zoom
- Node connection visualization
- Copy button for blueprint text

## Installation

Install the package with pip:

```bash
pip install mkdocs-blueprintue
```

## Usage

The plugin supports three ways to include blueprints in your markdown:

### 1. Code Block (Recommended)
This format supports editor code folding and syntax highlighting. You can optionally specify a custom height:

````markdown
```uebp height="500px"
Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_0"
   FunctionReference=(MemberName="PrintString",bSelfContext=True)
   NodePosX=0
   NodePosY=0
   NodeGuid=A0000000000000000000000000000000
End Object
```
````

The height parameter is optional and can be specified in:
- Pixels: `height="500px"`
- Em units: `height="30em"`
- Viewport height: `height="50vh"`

If not specified, a default height of 643px will be used.

### 2. Inline Blueprint Text
For shorter blueprints, you can use the inline syntax:

```markdown
![uebp]{{{Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_0" ... End Object}}}
```

Note: The inline syntax cannot be used inside code blocks.

### 3. Blueprintue.com Links
You can embed blueprints from blueprintue.com using their share links:

```markdown
![uebp]{{{https://blueprintue.com/render/your-blueprint-id/}}}
```

For example:
```markdown
![uebp]{{{https://blueprintue.com/render/50aau0g_/}}}
```

## Configuration

You can configure the plugin in your `mkdocs.yml`:

```yaml
plugins:
    - blueprintue:
        css_path: 'custom/css/path'  # Optional: custom path to CSS files
        js_path: 'custom/js/path'    # Optional: custom path to JavaScript files
```

## Changelog

### 0.1.4 (2024-12-25)
- Added support for custom height in code blocks using `height` parameter
- Fixed code block rendering in list items
- Added support for multiple CSS units (px, em, vh)

### 0.1.3 (2024-12-25)
- Fixed rendering issues in markdown list items
- Simplified textarea hiding method
- Fixed HTML escaping issues in JavaScript code

### 0.1.2 (2024-12-25)
- Fixed rendering issues in markdown list items
- Simplified textarea hiding method
- Fixed HTML escaping issues in JavaScript code

### 0.1.1 (2024-12-25)
- Fixed JavaScript code HTML escaping issues
- Improved code formatting and structure

### 0.1.0 (2024-12-25)
- Initial release
- Support for rendering local blueprint text
- Support for embedding blueprintue.com links
- Added copy-to-clipboard functionality
- Basic documentation and examples

## Project Status

 Core Features
- [x] Local blueprint rendering
- [x] Blueprintue.com embedding
- [x] Copy to clipboard functionality
- [x] Markdown list compatibility
- [x] Basic documentation

 Future Improvements
- [ ] Add support for custom height configuration
- [ ] Add support for dark/light theme switching
- [ ] Add support for custom styling options
- [ ] Improve error handling and user feedback
- [ ] Add more comprehensive documentation and examples

## Known Issues

Currently, there are no known major issues. If you encounter any problems, please [open an issue](https://github.com/ohiyo/mkdocs-blueprintue/issues).

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies: `pip install -e .[dev]`
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This plugin is based on [blueprintue-self-hosted-edition](https://github.com/blueprintue/blueprintue-self-hosted-edition), a fantastic project that provides the core functionality for rendering Unreal Engine Blueprint nodes. We are grateful to the original authors for their excellent work.

The blueprint rendering functionality has been extracted and adapted from the original project to work as a MkDocs plugin, while maintaining the same high quality and interactive features of the original implementation.



## Some Test Cases for Development

### 0. Code Block Style

```uebp
Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_0"
   FunctionReference=(MemberName="PrintString",bSelfContext=True)
   NodePosX=0
   NodePosY=0
   NodeGuid=A0000000000000000000000000000000
End Object
```

### 1.Code block Style In Item
- test
   ```uebp
      Begin Object Class=/Script/BlueprintGraph.K2Node_FunctionEntry Name="K2Node_FunctionEntry_0" ExportPath="/Script/BlueprintGraph.K2Node_FunctionEntry'/Game/YMyth/Scripts/EUB_Reparent.EUB_Reparent:Reparent.K2Node_FunctionEntry_0'"
      MetaData=(Category=NSLOCTEXT("", "0BB938DA40D01C31C087C781AA32C359", "AssetsTools"),bCallInEditor=True)
      LocalVariables(0)=(VarName="NewLocalVar",VarGuid=D6485B7348F22D545358DBB9D32BD8E5,VarType=(PinCategory="bool"),FriendlyName="New Local Var",Category=NSLOCTEXT("KismetSchema", "Default", "Default"),PropertyFlags=5)
      ExtraFlags=201457664
      FunctionReference=(MemberName="Reparent")
      bIsEditable=True
      NodePosX=-576
      NodePosY=-160
      NodeGuid=569AFD7742C04F4DBB29C4BCA53E3C6B
      CustomProperties Pin (PinId=DDFE266444E0867C353956AE6D8BF054,PinName="then",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_3 32442B704250EA76702B54BD34EDB28B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=9F616CC2469EE419F2782E948821970B,PinName="NewClass",Direction="EGPD_Output",PinType.PinCategory="class",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Knot_0 799C79824CDB5B36FF22A8A5E5F2A924,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties UserDefinedPin (PinName="NewClass",PinType=(PinCategory="class",PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'"),DesiredPinDirection=EGPD_Output)
   End Object
   Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="K2Node_CallFunction_3" ExportPath="/Script/BlueprintGraph.K2Node_CallFunction'/Game/YMyth/Scripts/EUB_Reparent.EUB_Reparent:Reparent.K2Node_CallFunction_3'"
      FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Blutility.EditorUtilityLibrary'",MemberName="GetSelectedAssets")
      NodePosX=-416
      NodePosY=-160
      NodeGuid=B3C52AB049B04542D551A789D6616C5F
      CustomProperties Pin (PinId=32442B704250EA76702B54BD34EDB28B,PinName="execute",PinToolTip="\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_FunctionEntry_0 DDFE266444E0867C353956AE6D8BF054,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=5E7C44C94C42D2912A232483BD4335AC,PinName="then",PinToolTip="\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_MacroInstance_0 1EBBA14142FF2284F9BB3783967A9EA6,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=B969F7D344A5327547DC5A965C7F7D1E,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nEditor Utility Library Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Blutility.EditorUtilityLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Blutility.Default__EditorUtilityLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=B6EDFA104E498D86131472950BAA9289,PinName="ReturnValue",PinToolTip="Return Value\nArray of Object References\n\nGets the set of currently selected assets",Direction="EGPD_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_MacroInstance_0 2BDB2A61497B7F0456302193D08D629E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   End Object
   Begin Object Class=/Script/BlueprintGraph.K2Node_MacroInstance Name="K2Node_MacroInstance_0" ExportPath="/Script/BlueprintGraph.K2Node_MacroInstance'/Game/YMyth/Scripts/EUB_Reparent.EUB_Reparent:Reparent.K2Node_MacroInstance_0'"
      MacroGraphReference=(MacroGraph="/Script/Engine.EdGraph'/Engine/EditorBlueprintResources/StandardMacros.StandardMacros:ForEachLoop'",GraphBlueprint="/Script/Engine.Blueprint'/Engine/EditorBlueprintResources/StandardMacros.StandardMacros'",GraphGuid=99DBFD5540A796041F72A5A9DA655026)
      NodePosX=-192
      NodePosY=-160
      NodeGuid=037C72AB4CFE12E44744F9B1C55BA907
      CustomProperties Pin (PinId=1EBBA14142FF2284F9BB3783967A9EA6,PinName="Exec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_3 5E7C44C94C42D2912A232483BD4335AC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=2BDB2A61497B7F0456302193D08D629E,PinName="Array",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_3 B6EDFA104E498D86131472950BAA9289,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=0A29109E400291BF23B8C091BF5491D9,PinName="LoopBody",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_4 2536DFAC4AD1CC94793AC3BC7E0229E9,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=4E4BEF17426B29B1AFF038AC012664AB,PinName="Array Element",Direction="EGPD_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_4 48C711ED41A67ECE79E44D86319A189E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=F241CE6B47B524A41BA6CBAB936B8E2A,PinName="Array Index",Direction="EGPD_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
      CustomProperties Pin (PinId=862A1DAD4DC338F072CDEEA9B95CCA35,PinName="Completed",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_1 6C2C96394222813F8C8020856BEAF1D3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   End Object

   ```

### 2. Don't affect other code blocks
```cpp
// Copyright Epic Games, Inc. All Rights Reserved.

#include "LyraConfirmationScreen.h"

#if WITH_EDITOR
#include "CommonInputSettings.h"
#include "Editor/WidgetCompilerLog.h"
#endif
// Create Attribute set
UPCGParamData* ParamData = NewObject<UPCGParamData>();
// Create an int32 attribute
FPCGMetadataAttribute<int32>* Attribute = ParamData->Metadata->CreateAttribute<int32>(TEXT("ChosenPointsNum"), NumberOfElementsToKeep, true, true);
// Assign value
Attribute->SetValue(ParamData->Metadata->AddEntry(), NumberOfElementsToKeep); 
```

### 3. No conversion inside code blocks

```txt

   ![uebp]{{{node text}}}
 
```

### 4. inline url test

![uebp]{{{https://blueprintue.com/render/50aau0g_/}}}

- ![uebp]{{{https://blueprintue.com/render/50aau0g_/}}}
