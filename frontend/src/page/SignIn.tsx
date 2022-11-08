import * as React from "react";
import { useCallback, useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";
import { TextField } from "@mui/material";
import paths from "../constant/path";
import { AppDispatch } from "../store";
import { selectUser, userActions } from "../store/slices/user";


export default function SignIn() {
  const navigate = useNavigate();
  const users = useSelector(selectUser).users;
  const loginUser = useSelector(selectUser).loginUser;
  const dispatch = useDispatch<AppDispatch>();
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  useEffect(() => {
    if (loginUser) {
      navigate(paths.search);
    }
  }, [navigate, loginUser]);

  const loginOnClick = useCallback(() => {
    const verifiedUser = users.find((user) => (user.email === email));
    if (verifiedUser) {
      dispatch(userActions.login(verifiedUser));
      navigate(paths.search);
    }
    else {
      alert("이메일이 틀렸습니다.");
    }
  }, [users, email, dispatch, navigate]);

  return (
    <section className={"h-screen w-full mt-12 mb-16"}>
      <section className={"h-screen w-full h-[32rem] flex flex-col"}>
        <h1 className={"text-center text-5xl text-pink-500 font-bold mt-24 my-16"}>
          두근두근<br />
          캠퍼스
        </h1>
        <div className={"flex flex-row place-content-center"}>
          <article className={"flex-initial w-24 text-pink-500 font-bold text-center leading-10"}>
            이메일:
          </article>
          <TextField
            sx={{
              maxWidth: 320,
              minWidth: 200,
            }}
            size={"small"}
            label={""}
            variant={"outlined"}
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
            }}
            required
          />
        </div>
        <div className={"flex flex-row place-content-center mt-6 mb-24"}>
          <article className={"flex-initial w-24 text-pink-500 font-bold text-center leading-10"}>
            비밀번호:
          </article>
          <TextField
            sx={{
              maxWidth: 320,
              minWidth: 200,
            }}
            size={"small"}
            label={""}
            variant={"outlined"}
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            required
          />
        </div>
      </section>
      <section className={"text-center"}>
        <div>
          <button
            className={"bg-pink-500 text-center text-white w-36 h-12 rounded-md"}
            disabled={!email || !password}
            onClick={loginOnClick}
          >
            로그인
          </button>
        </div>
        <div>
          <button
            className={"bg-white-500 text-center text-pink-400 border-solid border-b-4 border-l-2 border-r-2 mt-2 w-36 h-12 rounded-md"}
            onClick={() => navigate(paths.signUp)}
          >
            회원가입
          </button>
        </div>
      </section>
    </section>
  );
}
