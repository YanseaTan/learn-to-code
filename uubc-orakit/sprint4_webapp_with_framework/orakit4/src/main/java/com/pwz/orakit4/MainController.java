package com.pwz.orakit4;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class MainController {

    @RequestMapping("/")
    public ModelAndView root(){
        System.out.println("root()");
        return new ModelAndView("index.html");
    }

    @RequestMapping("/redirect")
    public String redirect(){
        System.out.println("redirect()");
        return "redirect:index.html";
    }

    @PostMapping("/chat")
    @ResponseBody
    public String chat(@RequestBody String input) {
        System.out.println("chat()");
        System.out.println("INPUT:\n" + input);
        return "default response from chatbot";
    }

}
