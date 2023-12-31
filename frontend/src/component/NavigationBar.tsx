import React, { useCallback, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ChatBubbleOutlinedIcon from "@mui/icons-material/ChatBubbleOutlined";
import FavoriteOutlinedIcon from "@mui/icons-material/FavoriteOutlined";
import GroupOutlinedIcon from "@mui/icons-material/GroupOutlined";
import { BottomNavigation, BottomNavigationAction, Paper } from "@mui/material";
import path from "../constant/path";
import style from "../constant/style";


type TabIndex = 0 | 1 | 2;

interface IProps {
  saveYPosition?: () => void;
}

export default function NavigationBar({
  saveYPosition,
}: IProps) {
  const navigate = useNavigate();
  const pathName = window.location.pathname;

  const getTabIndex = useCallback((pathName: string): TabIndex => {
    let newSelectedTab: TabIndex = 0;
    if (pathName.startsWith(path.search)) {
      newSelectedTab = 0;
    }
    else if (pathName.startsWith(path.pitapat)) {
      newSelectedTab = 1;
    }
    else if (pathName.startsWith(path.chat)) {
      newSelectedTab = 2;
    }
    return newSelectedTab;
  }, []);

  const [selectedTab, setSelectedTab] = useState<TabIndex>(getTabIndex(pathName));
  const [currentTab, setCurrentTab] = useState<TabIndex>(getTabIndex(pathName));

  useEffect(() => {
    setSelectedTab(getTabIndex(pathName));
  }, [pathName, getTabIndex]);

  useEffect(() => {
    let targetPath = "";

    if (currentTab === 0) {
      targetPath = "/search";
    }
    else if (currentTab === 1) {
      targetPath = "/pitapat";
    }
    else {
      targetPath = "/chat";
    }

    if (selectedTab !== currentTab) {
      navigate(targetPath);
    }
  }, [selectedTab, currentTab, navigate]);

  return (
    <Paper
      sx={{
        position: "fixed",
        bottom: 0,
        left: 0,
        right: 0,
      }}
      elevation={3}
      onClick={saveYPosition}
    >
      <BottomNavigation
        className={"fixed bottom-0 w-full"}
        showLabels
        value={currentTab}
        onChange={(_, newValue) => {
          setCurrentTab(newValue);
        }}
        sx={{
          backgroundColor: style.color.mainLightRgb,
          "& .Mui-selected": {
            color: style.color.background,
          },
          "& .Mui-selected svg": {
            color: "white",
          },
        }}
      >
        <BottomNavigationAction label="탐색" icon={<GroupOutlinedIcon/>}/>
        <BottomNavigationAction label="두근" icon={<FavoriteOutlinedIcon/>}/>
        <BottomNavigationAction label="대화" icon={<ChatBubbleOutlinedIcon/>}/>
      </BottomNavigation>
    </Paper>
  );
}
